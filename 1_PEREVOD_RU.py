from deep_translator import GoogleTranslator

En = "Good morning"

# Перевод текста с английского на русский
translator = GoogleTranslator(source='en', target='ru')
translated_text = translator.translate(En)

print(translated_text)  # переведите меня?