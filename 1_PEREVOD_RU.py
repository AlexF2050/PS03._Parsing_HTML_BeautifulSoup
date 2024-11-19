from deep_translator import GoogleTranslator

# Перевод текста с английского на русский
translator = GoogleTranslator(source='en', target='ru')
translated_text = translator.translate('translate me?')

print(translated_text)  # переведите меня?