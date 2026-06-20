from deep_translator import GoogleTranslator

def translate_to_english(text: str) -> tuple[str, str]:
    """
    Detects the language of the input text and translates it to English.
    Returns a tuple of (translated_text, original_language_code).
    """
    # GoogleTranslator automatically detects source language if set to 'auto'
    translator = GoogleTranslator(source='auto', target='en')
    translated = translator.translate(text)
    return translated, translator.source
