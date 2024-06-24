import telegram


def publishes_comics(token, path, ch_id):
    bot = telegram.Bot(token=token)
    with open(path, 'rb') as save_file:
        bot.send_document(chat_id=ch_id, document=save_file)
