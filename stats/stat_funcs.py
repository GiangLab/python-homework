import requests
from datetime import datetime

BASE_URL = 'http://localhost:5000'

#добавляет запись pk,user_id,datetime в таблицу
def add_data(id):
    url = f"{BASE_URL}/add"
    response = requests.post(url, json={'user_id': id})

    if response.status_code == 200:
        return "Data added successfully!"
    else:
        return f"Error {response.status_code}:{response.json().get('error')}"

#получает отчет за выбранную дату(тип -строка, формат - YYYY-MM-DD).
#По умолчанию сегодняшняя
def get_report(date=datetime.today().strftime('%Y-%m-%d')):
    url = f"{BASE_URL}/report"
    response = requests.get(url, params={'date': date})
    if response.status_code == 200:
        report = response.json().get('report')
        return report
    else:
        return f"Error {response.status_code}:{response.json().get('error')}"

#возвращает все данные из таблицы (select *)
def get_data():
    url = f"{BASE_URL}/data"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('data')
        return data
    else:
        return f"Error {response.status_code}:{response.json().get('error')}"

#очищает таблицу (truncate)
def flush_data():
    url = f"{BASE_URL}/flush"
    response = requests.post(url)
    if response.status_code == 200:
        return "Data flushed successfully!"
    else:
        return f"Error {response.status_code}"
