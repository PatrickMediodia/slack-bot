import os
# Use the package we installed
from slack_bolt import App
from slack_sdk import WebClient

# Initialize your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
channel_id = os.environ.get("CHANNEL_ID")

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
    try:
        result = client.chat_postMessage(
            channel=channel_id,
            text=message
            # You could also use a blocks[] array to send richer content
        )
        # Print result, which includes information about the message (like TS)
        print(result)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 5001)))
