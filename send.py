from telebot import TeleBot
import json
import os

with open('data.json') as f:
    templates = json.load(f)

content = templates.get('content')
channel = templates.get('tg-channel')

token = '7137779818:AAFTAK4lt2wT8tCv-jHuq5twCy91yLw6N6Q'

bot = TeleBot(token=token)

uploads_dir = 'uploads'
files = os.listdir(uploads_dir)
if (files):
    files.sort(key=lambda x: os.path.getmtime(os.path.join(uploads_dir, x)), reverse=True)
    latest_file = files[0]

    photo_path = os.path.join(uploads_dir, latest_file)
    photo = open(photo_path, 'rb')
    photo_message = bot.send_photo(channel, photo, caption=content)
    photo.close()

    bot.send_message(channel, content, photo_message)
    for filename in os.listdir('uploads'):
        file_path = os.path.join('uploads', filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f'Файл {file_path} успешно удален.')
else:
    bot.send_message(channel, content)

