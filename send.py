import telebot
import json
import vk_api

with open('data.json') as f:
    templates = json.load(f)

socset = templates.get('socset')
token = templates.get('token')
content = templates.get('content')

def post_on_wall(message, owner_id, access_token):
    vk_session = vk_api.VkApi(token=access_token)
    vk = vk_session.get_api()
    vk.wall.post(owner_id=owner_id, message=content)

post_on_wall(content, owner_id=219654837, access_token='vk1.a.R66uenWLlwwj4MSt1s5Bshn-FHtz3JCP2a7Q0HzkLRtBwafLRdPDFu78pgdfIEH3eo1nwbprQ0SpJoK9gArUg28juYUEWiYAmJrUY8YbnogR_kU8SQqMpzwVAsuH42WNFF6qYoFpaVYfK-m7rMZjNsy4rsKe1Ydr-dwxQCeOIIbfx5L0VT1y3bSv8kYuC90QpEkZG5kH0BmY0zNpohHThA')

# chat_id = '987609477'
# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['send'])
# def send_post():
#     bot.send_photo(chat_id, content)