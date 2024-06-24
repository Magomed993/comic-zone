import requests
import os
import random
import shutil
import argparse
from publication_telegram_bot import publishes_comics
from helper_script import download_file
from dotenv import load_dotenv


def get_latest_xkcd_comic_number():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    latest_issue_comic = response.json()['num']
    return latest_issue_comic


def get_image(comic_number):
    url = f'https://xkcd.com/{comic_number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    image = response.json()['img']
    return image


def main():
    load_dotenv()
    telega_api = os.environ['TG_BOT_TOKEN_COMICS']
    chat_id = os.environ['TG_CHAT_ID_COMICS']
    os.makedirs('images', exist_ok=True)
    parse = argparse.ArgumentParser(description='''Отправляет случайный комикс. 
        Есть возможность отправить конкретный комикс прописав дополнительный аргумент с номером комикса''')
    parse.add_argument('-n', '--number', help='comic number')
    args = parse.parse_args()
    try:
        if args.number is None:
            random_number = random.randint(1, get_latest_xkcd_comic_number())
            path = f'images/comic_{random_number}.png'
            download_file(get_image(random_number), path)
        else:
            path = f'images/comic_{args.number}.png'
            download_file(get_image(args.number), path)
        publishes_comics(telega_api, path, chat_id)
    finally:
        shutil.rmtree('images', ignore_errors=False)


if __name__ == '__main__':
    main()
