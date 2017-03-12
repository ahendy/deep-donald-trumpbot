from flask import Flask
from flask import request

import sys
import os
sys.path.append("..")

from fbmsgbot.bot import Bot
from fbmsgbot.models.message import Message
from fbmsgbot.models.template import Template
from fbmsgbot.models.attachment import Button, Element, ReceiptElement 
import json
import markovify

class TrumpBot(Bot):
	def __init__(self, text_model=None):
		super(TrumpBot, self).__init__(os.environ['token'])
		path = '../../recent.txt'
		with open(path) as f:
			text = f.read()
			# Build the model.
			text_model = markovify.Text(text)
			self.text_model = text_model


app = Flask(__name__)
bot = TrumpBot(os.environ['token'])

def set_welcome():
    response, error = bot.set_welcome("Donaldo Here")


@app.route('/', methods=['GET', 'POST'])
def webhook():
    # For webhook verification when registering app 
    if request.args.get("hub.verify_token") == "test_token":
        return request.args.get("hub.challenge")

    # Recieve a list of available messages
    msgs = bot.messages_for_request(request)
    for msg in msgs:
    	to = msg.sender

    	resp = bot.text_model.make_short_sentence(140)
    	msg = Message('text', resp)
    	bot.send_message(msg, to)

    return 'OK'

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
