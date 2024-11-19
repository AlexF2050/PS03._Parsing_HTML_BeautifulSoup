from bs4 import BeautifulSoup
import requests
from googletrans import Translator


# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)  # Запрос отправлен
        response.raise_for_status()  # Проверка на успешный ответ

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")

        # Получаем слово
        english_word = soup.find("div", id="random_word")
        word_definition = soup.find("div", id="random_word_definition")

        if english_word and word_definition:  # Проверяем, что нашли оба элемента
            return {
                "english_words": english_word.text.strip(),
                "word_definition": word_definition.text.strip()
            }
        else:
            print("Не удалось найти слово или его определение.")
            return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    translator = Translator()
    while True:
        # Получаем результат функции-словаря
        word_dict = get_english_words()
        if word_dict is None:  # Проверяем, была ли ошибка
            print("Попробуйте снова позже.")
            break

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и определение на русский язык
        translated_word = translator.translate(word, dest='ru').text
        translated_definition = translator.translate(word_definition, dest='ru').text

        # Начинаем игру
        print(f"Значение слова - {translated_definition}")
        user = input("Что это за слово? ")
        if user.lower() == word.lower():  # Игнорируем регистр
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {translated_word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n: ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


word_game()  # Запускаем игру