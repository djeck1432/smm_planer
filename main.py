from __future__ import print_function
import pickle
import os.path
import time
import datetime
import os
import telegram
import vk_api
import extracturl
import facebook
from urllib.parse import urlparse
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dotenv import load_dotenv

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SAMPLE_RANGE_NAME = 'A:H'
DAYS_OF_THE_WEEK = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресения': 6,
}
PUBLISH_OR_NOT = {'да': True, 'нет': False}


def google_sheets(spread_sheet_id):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spread_sheet_id,
                                range=SAMPLE_RANGE_NAME, valueRenderOption='FORMULA').execute()
    values = result.get('values')
    return values


def google_sheets_update(spread_sheet_id, sheet_index):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    values = [
        [
            'да'
        ],

    ]
    body = {
        'values': values
    }
    service = build('sheets', 'v4', credentials=creds)
    result = service.spreadsheets().values().update(
        spreadsheetId=spread_sheet_id, range='H' + str(sheet_index),
        valueInputOption='RAW', body=body).execute()


def get_link_formatted(link):
    if '=HYPERLINK("' in link:
        text = link.split('"')
        url = urlparse(text[1])
        url_id = url.query.strip('id=')
    else:
        link = extracturl.extract(link)
        url = urlparse(link)
        url_id = url.query.strip('id=')
    return url_id


def get_post_informations():
    date = datetime.datetime.now()
    today = date.weekday()
    hours = date.hour
    values = google_sheets()
    post_params = []
    if not values:
        print('No data found.')
    else:
        for sheet_index, value in enumerate(values[2:]):
            if DAYS_OF_THE_WEEK[value[3]] == today and value[4] == hours:
                post_params.append({
                    'vk': value[0],
                    'tg': value[1],
                    'fb': value[2],
                    'publish_day': DAYS_OF_THE_WEEK[value[3]],
                    'publish_time': value[4],
                    'publish_article': get_link_formatted(value[5]),
                    'publish_image': get_link_formatted(value[6]),
                    'is_published': value[7],
                    'sheet_index': sheet_index + 2,
                })
    return post_params


def download_google_drive(drive, publish_article, publish_image):
    name_of_file = {}
    if publish_image is not None:
        file_image = drive.CreateFile({'id': publish_image})
        file_image.GetContentFile(file_image['title'])
        name_of_file['name_image'] = file_image['title']
    if publish_article is not None:
        file_text = drive.CreateFile({'id': publish_article})
        file_text.GetContentFile(file_text['title'], mimetype='text/plain')
        name_of_file['name_text'] = file_text['title']

    return name_of_file


def post_telegram(bot, telegram_chat_id, image, text):
    with open(text, 'r') as text:
        bot.send_message(chat_id=telegram_chat_id, text=text.read())
    with open(image, 'rb') as photo:
        bot.send_photo(chat_id=telegram_chat_id, photo=photo)


def post_vkontakte(vk_phone, vk_password, vk_owner_id, vk_album_id, image_path, text):
    vk_session = vk_api.VkApi(vk_phone, vk_password)
    vk = vk_session.get_api()
    vk_session.auth()
    upload = vk_api.VkUpload(vk_session)
    owner_id = '-' + vk_owner_id
    photo = upload.photo(
        image_path,
        group_id=vk_owner_id,
        album_id=vk_album_id
    )
    attachment_photo = 'photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])
    with open(text, 'r') as text:
        return vk.wall.post(owner_id=owner_id, message=text.read(), attachment=attachment_photo)


def post_facebook(facebook_token, facebook_group_id, image_path, text):
    graph = facebook.GraphAPI(access_token=facebook_token, version='3.1')
    with open(image_path, 'rb') as image:
        with open(text, 'r') as text:
            graph.put_photo(image=image, album_path=facebook_group_id + '/photos', message=text.read())


def main():
    load_dotenv()
    # telegram secret keys
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(token=telegram_token)

    # vk secret keys
    vk_phone = os.getenv('VK_PHONE')
    vk_password = os.getenv('VK_PASSWORD')
    vk_owner_id = os.getenv('VK_OWNER_ID')
    vk_album_id = os.getenv('VK_ALBUM_ID')

    # fb secret keys
    facebook_token = os.getenv('FACEBOOK_TOKEN')
    facebook_group_id = os.getenv('FACEBOOK_GROUP_ID')

    spread_sheet_id = os.getenv('SPREAD_SHEET_ID')
    google_sheets(spread_sheet_id)
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    while True:
        posts = get_post_informations()
        for post in posts:
            publish_vk = PUBLISH_OR_NOT[post['vk']]
            publish_tg = PUBLISH_OR_NOT[post['tg']]
            publish_fb = PUBLISH_OR_NOT[post['fb']]
            name_of_file = download_google_drive(drive, post['publish_article'], post['publish_image'])
            if not PUBLISH_OR_NOT[post['is_published']]:
                if publish_tg:
                    post_telegram(bot, telegram_chat_id, name_of_file['name_image'], name_of_file['name_text'])
                if publish_vk:
                    post_vkontakte(vk_phone, vk_password, vk_owner_id, vk_album_id, name_of_file['name_image'],
                                   name_of_file['name_text'])
                if publish_fb:
                    post_facebook(facebook_token, facebook_group_id, name_of_file['name_image'], name_of_file['name_text'])
                google_sheets_update(spread_sheet_id, post['sheet_index'])
        time.sleep(1800)


if __name__ == '__main__':
    main()


