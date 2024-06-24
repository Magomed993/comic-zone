import requests


def download_file(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


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
