from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('ZuX8m+OITcOXB+dDcmvCknrsbtUJ+c7mJwQubVFwlNFNct8c/YEORet/X4giQdezRDd/Ysb30DwBZV1Kjxx8oMRlI+koo3ZkWUFZIyQ6RIBmuxMzX/LmUBQf58EskP6hY5ixgr27JKJnxE3ZXS1acAdB04t89/1O/w1cDnyilFU=')
handler1 = WebhookHandler('15b26426acc8b137890028c8d4f1eef1')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler1.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler1.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
