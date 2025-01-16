from googletrans import Translator

def translate_text(text,language):
    """
  Перевести текст с любого языка на русский и английский.
    Args:
        text (str): Текст для перевода.
        language 
        'ru' - на русский
        'en' - на английский
    Returns:
        str:Текст переведен на русский язык
    """
    # Initialize Translator object
    translator = Translator()

    try:
        # Translate text into Russian
        translation = translator.translate(text, dest=language)

        # Check if the returned result is a list or not
        if isinstance(translation, list):
            translated_text = [t.text for t in translation]
        else:
            translated_text = translation.text
        
        # Cast to string and return result
        return str(translated_text).strip()

    except Exception as e:
        return "#4" #f"Error during translation: {e}"