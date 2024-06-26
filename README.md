# Зона комиксов
Программа позволяет скачивать и публиковать комиксы в телеграмм канале.
## Как установить
Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Создать телеграм канал и бота согласно [инструкции](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/).
## Окружения
Сгенерировать в мессенджере телеграм `API token` и его адрес у [Отца Ботов](https://telegram.me/BotFather).
## Переменные окружения
Сгенерированный у [Отца Ботов](https://telegram.me/BotFather) `API token` необходим для установления переменной окружения в секретный файл формата `.env`.
### Как получить
![Снимок экрана (15)](https://github.com/Magomed993/comic-zone/assets/160238040/8c7d1e7c-d451-4e26-91e5-8cd54fca569c)
1. Создай файл `.env` в корневом каталоге проекта, если он ещё не существует. Обычно это делается в корневой папке проекта, где находится основной исполняемый файл или файл конфигурации.
2. Откройте файл `.env` в текстовом редакторе и добавьте в него переменные окружения, как показано выше. Убедитесь, что переменные и их значения разделены знаком = без пробелов.
3. Убедитесь в установке с файла `requirements.txt` библиотеки `python-dotenv` для загрузки переменных окружения из файла `.env`.

Теперь у вас должен быть файл `.env`, содержащий все необходимые переменные окружения для корректной работы.\
Данные переменные необходимы для корректной работы программы. От них зависит полномерность выведения данных вакансий на экран.
## Скрипты и их запуск
```
python publishing_comics_telegram.py
```
- скрипт скачивает в случайном порядке комикс и публикует в телеграмм канале в бесконечном цикле один раз в час. Если прописать дополнительный аргумент можно скачать и опубликовать под отдельным номером комикс;
```
python publishing_one_comic_telegram.py
```
- скрипт скачивает один в случайном порядке комикс и публикует его в телеграмм канале. Если прописать дополнительный аргумент можно скачать и опубликовать под отдельным номером комикс;
```
helper_script.py
```
- вспомогательный скрипт, необходимый для скачивания комиксов.
```
publication_telegram_bot.py
```
- скрипт , с помощью которого происходит связь с телеграм ботом и публикацией комиксов.
## Примечания
Пример работы данного проекта на ОС Windows через cmd:
![GIF 23 06 2024 13-41-30](https://github.com/Magomed993/comic-zone/assets/160238040/da093fa6-c88b-4729-b548-21abfe171eda)

