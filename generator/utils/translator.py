from deep_translator import GoogleTranslator

def translate_to_english(text: str) -> tuple[str, str]:
    """
    Translates text to English and returns the translated text along with the source language code.
    """
    try:
        translator = GoogleTranslator(source='auto', target='en')
        translated = translator.translate(text)
        return translated, translator.source
    except Exception as e:
        return text, f"translation_error ({e})"
      
