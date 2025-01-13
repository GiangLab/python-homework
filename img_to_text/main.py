import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import os

# Функция для настройки пути к Tesseract (только для Windows)
def set_tesseract_path():
    try:
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        print("Путь к Tesseract установлен.")
    except Exception as e:
        print(f"Ошибка установки пути к Tesseract: {e}")

# Функция для обработки изображения
def process_image(image_path):
    try:
        # Загрузка изображения
        image = Image.open(image_path)
        print(f"Загружено изображение: {image_path}")

        # Предобработка изображения
        image = image.convert("L")  # Преобразование в оттенки серого
        image = image.filter(ImageFilter.SHARPEN)  # Повышение резкости

        # Опционально: улучшение контрастности
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2.0)  # Увеличение контрастности

        return image
    except Exception as e:
        print(f"Ошибка обработки изображения: {e}")
        return None

print("Выберите язык для распознавания: \n 1: Русский \n 2: Английский")
choice = input("Введите номер языка: ")

if choice == "1":
    lang = "rus"
elif choice == "2":
    lang = "eng"
else:
    print("Неверный выбор. Используется английский язык по умолчанию.")
    lang = "eng"


# Функция для распознавания текста на двух языках
def recognize_text(image, languages=lang):
    try:
        print(f"Распознавание текста на языках: {languages}")
        text = pytesseract.image_to_string(image, lang=languages)
        return text
    except Exception as e:
        print(f"Ошибка распознавания текста: {e}")
        return ""

# Функция для записи текста в файл
def save_text_to_file(text, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Распознанный текст сохранен в файл: {output_file}")
    except Exception as e:
        print(f"Ошибка сохранения текста в файл: {e}")

# Основная программа
def main():
    # Установите путь к Tesseract на Windows
    set_tesseract_path()

    # Укажите путь к изображению
    image_path = input("Введите путь к изображению: ")

    # Проверьте, существует ли файл
    if not os.path.exists(image_path):
        print("Файл не найден. Проверьте путь и попробуйте снова.")
        return

    # Обработайте изображение
    processed_image = process_image(image_path)
    if not processed_image:
        print("Не удалось обработать изображение.")
        return

    # Распознайте текст
    recognized_text = recognize_text(processed_image)

    # Вывод результата
    print("\nРаспознанный текст:")
    print(recognized_text)

    # Сохранение текста в файл
    output_file = "recognized_text.txt"
    save_text_to_file(recognized_text, output_file)

if __name__ == "__main__":
    main()
