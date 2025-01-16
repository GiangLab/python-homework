import sqlite3
from users import User
from datetime import datetime

# добавление пользователя в user с user_id и name
def userAdd(userInfo):
    conn =sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO user (user_id, name,registrateDate) VALUES ('%i','%s','%s')" % (userInfo.user_id,userInfo.name,userInfo.translateDate))
    conn.commit()
    cur.close()
 
# добавление информации о переводах пользователя в booking с user_id 
def userInformationAdd(userInfo):

    cur_dt = datetime.now()
    
    conn =sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO information (user_id, translateDate, directionOfTranslation, original, translation, inputType,\
                                          cur_year, cur_month, cur_day)\
                 VALUES ('%i','%s','%s','%s','%s','%s','%i','%i','%i')" % (userInfo.user_id, userInfo.translateDate, userInfo.directionOfTranslation, 
                                                                 userInfo.inputType, userInfo.original, userInfo.translation, 
                                                                 userInfo.cur_year, userInfo.cur_month, userInfo.cur_day))
    conn.commit()
    conn.close()


# поиск пользователя с user_id
def userSearch(user_id):
    # открываем таблицу user.db
    conn =sqlite3.connect("users.db")
    cur = conn.cursor()
    params = (user_id,)
    # ищем пользователя с user_id
    cur.execute("SELECT name FROM user WHERE user_id = ?", params)
    res = cur.fetchone()
    cur.close()
    
    # если таблица information для хранения информации о пользователи не существует создаем базу данных 
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS information(translate_id, user_id int,translateDate varchar(10),\
                 directionOfTranslation varchar(5), inputType  varchar(5), original text, translation text, \
                 cur_year int, cur_month int, cur_day int )')
    conn.commit()
    cur.close()   
    conn.close() 
    return res

# ежедневный отчет по пользователям
def reportСurrentDay():
   
    cur_dt = datetime.now()
    
    conn =sqlite3.connect("users.db")
    cur = conn.cursor()
    params = (cur_dt.year, cur_dt.month, cur_dt.day)
    cur.execute("SELECT user.name, information.* FROM information LEFT JOIN user USING (user_id) WHERE (cur_year = ?) AND (cur_month = ?) AND (cur_day = ?)", params)
    
    res = cur.fetchall()
    info = f'<b><i>Дата:</i> {cur_dt.day}.{ cur_dt.month}.{cur_dt.year}</b> \n'
    f=open('db.txt', 'a')
    for el in res:
    # 0- name, 1- translate_id, 2 - user_id , 3- translateDate,4- directionOfTranslation, 
    # 5 - inputType, 6- original , 7 - translation ,
    # 8- cur_year, 9 - cur_month , 10 - cur_day int )')
        info += f'<b>Пользователь: {el[0]},  параметры перевода:</b>\n'
        info += f'<b><i>дата перевода:</i> {el[10]}.{ el[9]}.{el[8]}</b> \n'
        if el[3]=='en_ru':
            info += f'• <i>перевод с английского на русский</i> \n'
        else:
            info += f'• <i>перевод с русского на английский</i> \n'
        if el[5]=='recognize':
            info += f'• <i>текст оригинала распознан</i>\n'
        else:
            info += f'• <i>текст оригинала введен</i>\n'
        info += f'• <i>оригинал:</i> <b>{el[6]}</b>\n'
        info += f'• <i>перевод</i>: <b>{el[7]}</b>\n'
        f.write(info)
    f.close
    cur.close()
    conn.close() 
    return info

# ежедневный отчет по пользователям
def reportСurrentUser(userInfo):
   
    cur_dt = datetime.now()
    
    conn =sqlite3.connect("users.db")
    cur = conn.cursor()
    params = (userInfo.user_id,)
    cur.execute("SELECT * FROM information WHERE user_id = ? ", params)
   
    res = cur.fetchall()
    info = f'<b><i>Пользователь:</i> {userInfo.name}, ID: {userInfo.user_id} </b> \n'
    f=open('db.txt', 'a')
    for el in res:
    # 0- translate_id, 1 - user_id , 2- translateDate,3- directionOfTranslation, 
    # 4 - inputType, 5- original , 6 - translation , # 7 cur_year, 8 - cur_month , 9 - cur_day int )')
        info += f'<b>параметры перевода:</b>\n'
        info += f'<b><i>дата перевода:</i> {el[9]}.{ el[8]}.{el[7]}</b> \n'
        if el[3]=='en_ru':
            info += f'• <i>перевод с английского на русский</i> \n'
        else:
            info += f'• <i>перевод с русского на английский</i> \n'
        if el[4]=='recognize':
            info += f'• <i>текст оригинала распознан</i>\n'
        else:
            info += f'• <i>текст оригинала введен</i>\n'
        info += f'• <i>оригинал:</i> <b>{el[5]}</b>\n'
        info += f'• <i>перевод</i>: <b>{el[6]}</b>\n'
        f.write(info)
    f.close
    cur.close()
    conn.close() 
    return info

def usersList():
    conn =sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute('SELECT user.user_id, user.name, COUNT(*) FROM information LEFT JOIN user USING (user_id) GROUP BY user.user_id, user.name')
    users = cur.fetchall()
    info = 'Статистика запросов по пользователям \n'
    for el in users:
        info += f'Пользователь: {el[1]}, id: {el[0]}, количество запросов: {el[2]} \n'
    cur.close()
    conn.close()
    return info
