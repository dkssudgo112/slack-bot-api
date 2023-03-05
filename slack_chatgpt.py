# -*- coding: utf-8 -*-

import openai
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from flask import Flask, request

openai.api_key = "YOUR_KEY"

# Replace with your Bot User OAuth Access Token
SLACK_BOT_TOKEN = "YOUR_SLACK_KEY"


# Initialize a WebClient instance
client = WebClient(token=SLACK_BOT_TOKEN)

# Initialize a Flask app instance
app = Flask(__name__)

# Handle incoming POST requests to the /bot-command endpoint
@app.route("/bot-command", methods=["POST"])
def handle_bot_command():
    payload = request.form.to_dict()
    if payload.get("command") == "/gpt":
        text = payload.get("text")
        print(text)
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": text}]
        )
        print(completion)
        text2 = completion.choices[0].message.content.strip()
        print(text2)
        try:
            response = client.chat_postMessage(channel="#07_rnd_알림", text=text+ "\n에 대한 대답은\n"+text2)
            return "", 200
        except SlackApiError as e:
            return f"Error: {e.response['error']}", 200
    else:
        return "", 200

if __name__ == "__main__":
    app.run(debug=True)







