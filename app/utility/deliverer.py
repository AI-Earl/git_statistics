import requests
import json

from config import config
from app.utility.logger import logger


class RequestManager:
    def __init__(self, url):
        self.url = url
        self.headers = {'Content-Type': 'application/json'}

    def post(self, data):
        result_json = {}
        try:
            response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
            response.raise_for_status()

            result_json = response.json()
        except Exception as e:
            logger.error(f"Error: {e.message if hasattr(e, 'message') else e}")

        return result_json


class LineBotMessenger(RequestManager):
    def __init__(self, channel_token, user_id):
        super().__init__(url='https://api.line.me/v2/bot/message/push')
        self.headers['Authorization'] = f'Bearer {channel_token}'
        self.user_id = user_id

    def send(self, message_type, text):
        message = {
            'type': message_type,
            'text': text
        }

        payload = {
            'to': self.user_id,
            'messages': [message]
        }

        return super().post(payload)


if __name__ == '__main__':
    line_bot_messenger = LineBotMessenger(config.LINE_BOT_TOKEN, config.LINE_BOT_USER_ID)
    line_bot_messenger.send('text', 'Hello World!\n1\n2\n3')
