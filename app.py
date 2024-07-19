import os
import time
import threading
from slack_bolt import App
from slack_sdk import WebClient

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

PORT = int(os.environ.get("PORT", 5001))
channel_id = os.environ.get("CHANNEL_ID")
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.event("message")
def reply_message(event, say):
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{event['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{event['user']}>!"
    )

def send_message(message):
    #tail log files
    try:
        result = client.chat_postMessage(
            channel=channel_id,
            text=message
        )
        print(result)
    except Exception as e:
        print(e)

    #mocked log file output values
    time.sleep(10)
    send_message(message)

if __name__ == "__main__":
    #start thread for sending tailed log files
    send_thread = threading.Thread(
        target=send_message,
        args=['hello'],
        daemon=True
    )

    # thread for listening to user commands
    listen_thread = threading.Thread(
        target=app.start,
        args=[PORT],
        daemon=True
    )

    listen_thread.start()
    send_thread.start()

    while True:
        continue