import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import os
import config

# Функция для настройки пути к Tesseract (только для Windows)
def set_tesseract_path():
    try:
        pytesseract.pytesseract.tesseract_cmd = config.PATH_Tesseract
        result = "Путь к Tesseract установлен."
        return result
    except Exception as e:
        result = '#3' #f"Ошибка установки пути к Tesseract: {e}"
        return result

# Функция для обработки изображения
def process_image(image_path):
    try:
        # Загрузка изображения
        image = Image.open(image_path)

        # Предобработка изображения
        image = image.convert("L")  # Преобразование в оттенки серого
        image = image.filter(ImageFilter.SHARPEN)  # Повышение резкости

        # Опционально: улучшение контрастности
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2.0)  # Увеличение контрастности

        return image
    except Exception as e:
        #print(f"Ошибка обработки изображения: {e}")
        return None


# Функция для распознавания текста на двух языках
# language:  "rus", "eng"
def recognize_text(image, language):
    try:
        #print(f"Распознавание текста на языках: {languages}")
        text = pytesseract.image_to_string(image, language)
        return text
    except Exception as e:
        
        return "#2" #print(f"Ошибка распознавания текста: {e}")

# Функция для записи текста в файл
def save_text_to_file(text, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Распознанный текст сохранен в файл: {output_file}")
    except Exception as e:
        print(f"Ошибка сохранения текста в файл: {e}")

# Основная функция
def recognize(PATH_img,language):
    # Установите путь к Tesseract на Windows
    result = set_tesseract_path()
    if result == '#3':
        return result ##f"Ошибка установки пути к Tesseract: {e}"

    # Укажите путь к изображению
    image_path = config.PATH_img

    # Проверьте, существует ли файл
    if not os.path.exists(image_path):
        return '#0' #print("Файл не найден. Проверьте путь и попробуйте снова.")

    # Обработайте изображение
    processed_image = process_image(image_path)
    if not processed_image:
        return '#1' #print("Не удалось обработать изображение.")

    # Распознайте текст
    recognized_text = recognize_text(processed_image,language)

    # Вывод результата
    return recognized_text

