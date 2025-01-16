# Приложение для телеграмм - бота "Система распознавания текста и перевод в другой язык"
(
Этот проект представляет собой Python-приложение телеграмм - бота
"Система распознавания текста и перевод в другой язык"

## Возможности
1. Ведение статистики по использованию ботом:
- Запись в таблицу пары user_id и времени когда он воспользовался ботом.
- Возможность просмотра обобщенной статистики: сколько каждый user_id воспользовался за день.
- Возможность очистки содержимого таблицы.
2. Распознования текста на изображении: 
- Распознавание текста на русском (rus) и английском (eng).
- Возможность выбора языка распознавания пользователем.
3. Перевод текста
- Возможность выбора языка перевода пользователем.
- Возможность выбора ввода текста (ввод с консоли или распознать текст на изображении)  
4. Возможность дополнения решения под собственные задачи
  
## Требования
Для запуска этого проекта локально необходимо:

1. Установленный Python версии 3.7 или новее.
2. Установленный docker.
3. Установленные библиотеки Python из файла `requirements.txt`.
4. Установленный [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) на вашей системе.
   - Убедитесь, что исполняемый файл Tesseract добавлен в PATH вашей системы.
   - Скачайте языковые модели `rus.traineddata` и `eng.traineddata` из [tessdata](https://github.com/tesseract-ocr/tessdata) и поместите их в папку `tessdata` установки Tesseract.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/GiangLab/python-homework.git
   cd python-homework
   cd translatorBot
   ```

2. Установите необходимые библиотеки Python:
   ```bash
   pip install -r requirements.txt
   ```

3. Установите Docker следуя инструкциям из [официальной документации](https://docs.docker.com/get-started/get-docker/?_gl=1*xf7d1i*_gcl_au*MTU1NTk1NzcyLjE3MzY5ODYyMzM.*_ga*MTA0NTc4MzAyNC4xNzI0MTU0OTAy*_ga_XJWPQMJYHQ*MTczNjk5MDc0NS41LjEuMTczNjk5MDc1Mi41My4wLjA)
4. Установите Tesseract OCR:
   - **Windows**: Скачайте установщик с [страницы загрузок Tesseract для Windows](https://github.com/UB-Mannheim/tesseract/wiki).
   - **MacOS**: Установите через Homebrew:
     ```bash
     brew install tesseract
     ```
   - **Linux**: Установите через менеджер пакетов, например, на Ubuntu:
     ```bash
     sudo apt install tesseract-ocr 
     ```
     
## Использование

1. Запустите Docker desktop 
2. Постройте и запустите образ контейнера:
   ```bash
   docker-compose up --build
   ```