from flask import Flask, jsonify, request
import psycopg2
import os
from datetime import datetime, timedelta

app = Flask(__name__)

# Конфигурация подключения к PostgreSQL
DATABASE_URL = os.getenv('DATABASE_URL',
                         'postgresql://user:password@db:5432/testdb')


# Подключение к базе данных
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn


# функция исполнения простого запроса
def execute_query(query, params=None, res=False):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    if res == True:
        results = cur.fetchall()  # Получаем все строки
    else:
        results = None
    conn.commit()
    cur.close()
    conn.close()
    return results


# Создание таблицы, если она не существует
def create_table():
    execute_query("""
        CREATE TABLE IF NOT EXISTS user_activity (
            pk SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            date TIMESTAMP NOT NULL
        );
    """)


#функция записи в базу данных
@app.route('/add', methods=['POST'])
def add_data():
    data = request.json.get('user_id')
    if not data:
        return jsonify({"error": "No user_id provided"}), 400

    current_date = datetime.now() + timedelta(hours=3)


    execute_query("INSERT INTO user_activity (user_id, date) VALUES (%s, %s)",
                  (data, current_date))

    return jsonify({"message": "Data added successfully!"})

#функция опустошения базы данных
@app.route('/flush', methods=['POST'])
def flush_data():
    execute_query("Truncate table user_activity ")
    return jsonify({"message": "Data flushed successfully!"})


# Простейшая функция для генерации отчета по данным
@app.route('/report', methods=['GET'])
def generate_report():
    date_str = request.args.get('date')
    if not date_str:
        return jsonify({"error": f"No date provided"}), 400

    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    rows = execute_query("""
        SELECT user_id, COUNT(*) 
        FROM user_activity 
        WHERE DATE(date) = %s 
        GROUP BY user_id
    """, (date,), res=True)

    # Генерация отчета
    report = f"Статистика запросов по пользователям на {date} \n"
    for user_id, count in rows:
        report += f'Пользователь {user_id}: количество запросов: {count} \n'

    return jsonify({"report": report})


@app.route('/data', methods=['GET'])
def get_data():
    rows = execute_query("SELECT * FROM user_activity",res=True)
    return jsonify({"data": rows})


if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', port=5000)
