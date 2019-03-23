from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify

from data_api_bot import *

import requests
import json
import datetime

app=Flask(__name__)
sslify=SSLify(app)

#Class with the main functions of the bot
#Класс с основными функциями бота
class BotHandler:
        def __init__(self, token):
                self.token = token
                self.api_url = "https://graph.facebook.com/v3.2/"
        def send_message(self,sender_id,message):
            data = json.dumps({"recipient": {"id": sender_id},"message": {"text": message}})
            params={"access_token":token}
            headers = {"Content-Type": "application/json"}
            res=requests.post(self.api_url + "me/messages",params=params,headers=headers,data=data)
        def get_user(self,sender_id):
            params={"access_token":token}
            res=requests.get(self.api_url + f"{sender_id}",params=params).json()
            return res["first_name"]

bot = BotHandler(token)

@app.route('/', methods=['GET','POST'])
def actions():
    if request.method=='POST':
        now = datetime.datetime.now()
        data = request.get_json()
        entry = data['entry'][0]
        if entry.get("messaging"):
            messaging = entry['messaging'][0]
            last_user_id = messaging['sender']['id']
            try:
                last_message = messaging['message']['text']
                #Welcome bot depending on the time of day with a time shift
                #Приветствие бота в зависимости от времени суток со сдвигом по времени
                if last_message.lower() in greetings and 6 <= now.hour+2 < 12:
                    bot.send_message(last_user_id,f'Доброе утро, {bot.get_user(last_user_id)}!')
                elif last_message.lower() in greetings and 12 <= now.hour+2 < 17:
                    bot.send_message(last_user_id,f'Доброе день, {bot.get_user(last_user_id)}!')
                elif last_message.lower() in greetings and 17 <= now.hour+2 < 23:
                    bot.send_message(last_user_id,f'Доброе вечер, {bot.get_user(last_user_id)}!')
                elif last_message.lower() in greetings and ((now.hour+2)>=23 or (now.hour+2)<6):
                    bot.send_message(last_user_id,f'Доброго времени суток, {bot.get_user(last_user_id)}!')
            except KeyError:
                pass
    return 'ok', 200

if __name__ == '__main__':
    app.run()
