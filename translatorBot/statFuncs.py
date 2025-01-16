import requests
from datetime import datetime

BASE_URL = 'http://localhost:5000'


def add_data(id):
    """добавляет запись pk,user_id,datetime в таблицу"""
    url = f"{BASE_URL}/add"
    response = requests.post(url, json={'user_id': id})

    if response.status_code == 200:
        return "Data added successfully!"
    else:
        return f"Error {response.status_code}"


def get_report(date: str = datetime.today().strftime('%Y-%m-%d')):
    """Возвращает отчёт за выбранную дату (формат - YYYY-MM-DD).
      По умолчанию сегодняшняя"""
    url = f"{BASE_URL}/report"
    response = requests.get(url, params={'date': date})
    if response.status_code == 200:
        report = response.json().get('report')
        return report
    else:
        return f"Error {response.status_code}:{response.json().get('error')}"


def get_data():
    """возвращает все данные из таблицы (select *)"""
    url = f"{BASE_URL}/data"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('data')
        return data
    else:
        return f"Error {response.status_code}:{response.json().get('error')}"


def flush_data():
    """очищает таблицу (truncate)"""
    url = f"{BASE_URL}/flush"
    response = requests.post(url)
    if response.status_code == 200:
        return "Data flushed successfully!"
    else:
        return f"Error {response.status_code}"
