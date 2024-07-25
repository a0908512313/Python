from flask import Flask, request
import json

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
app = Flask(__name__)


def linebot():
    body = request.get_data(as_text=True)
    try:
        json_data = json.loads(body)
        access_token = 'Dcgn3kC2RAcF6DtWIonkzJuejRDVMcqXrH3vBYoVablUMVwEXULx71EzBdhNoAHzCXXv+i3e0e5+1XusNWUSOB+IrVUvdYrg+R/D8W21Fmz2qkYoUkYYjG9qNIjvsJOapAOy3b/jLJxcz3mImuRiXwdB04t89/1O/w1cDnyilFU='
        secret = 'd7a7b81c585e1351d44c646dc8ad4e96'
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(secret)
        signature = request.headers['X-Line_Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['token']
        type = json_data['events'][0]['message']['type']
        if type == 'text':
            msg = json_data['events'][0]['message']['text']
            print(msg)
            reply = msg
        else:
            reply = "Not text~~"

        print(reply)
        line_bot_api.reply_message(tk, TextSendMessage(reply))

    except:
        print(body)

    return "OK"


if __name__ == '__main__':
    app.run()
