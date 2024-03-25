import json
import os
import vk_api
import requests

with open('data.json') as f:
    templates = json.load(f)

content = templates.get('content')
token = templates.get('access-token-vk')
owner_id = templates.get('vk-id')

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

if os.path.isdir('uploads'):
    files = os.listdir('uploads')

    if files:
        files.sort(key=lambda x: os.path.getmtime(os.path.join('uploads', x)), reverse=True)

        latest_file = files[0]
        photo_path = os.path.join('uploads', latest_file)

        upload_url = vk.photos.getWallUploadServer(group_id=owner_id[1:])['upload_url']

        with open(photo_path, 'rb') as photo:
            response = requests.post(upload_url, files={'photo': photo}).json()

        photo_data = vk.photos.saveWallPhoto(group_id=owner_id[1:], photo=response['photo'], server=response['server'],
                                             hash=response['hash'])[0]

        attachment = f"photo{photo_data['owner_id']}_{photo_data['id']}"
    else:
        attachment = None

    vk.wall.post(owner_id=owner_id, message=content, attachments=attachment)
    for filename in os.listdir('uploads'):
        file_path = os.path.join('uploads', filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f'Файл {file_path} успешно удален.')
else:
    vk.wall.post(owner_id=owner_id, message=content)
