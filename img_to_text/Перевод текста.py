from googletrans import Translator

def translate_to_russian(text):
    """
  Перевести текст с любого языка на русский.

    Args:
        text (str): Текст для перевода.
        
    Returns:
        str:Текст переведен на русский язык
    """
    # Initialize Translator object
    translator = Translator()

    try:
        # Translate text into Russian
        translation = translator.translate(text, dest='ru')

        # Check if the returned result is a list or not
        if isinstance(translation, list):
            translated_text = [t.text for t in translation]
        else:
            translated_text = translation.text
        
        # Cast to string and return result
        return str(translated_text).strip()

    except Exception as e:
        return f"Error during translation: {e}"