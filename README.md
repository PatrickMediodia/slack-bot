# Alerts Slack Bot

## Ideas
- List of ideas to be implemented in the future
- [Link](Ideas.md)

## Ran Using Ngrok for Development:

#### Run the slack bot (Running on port 5001)
```
python app.py
```

#### Expose and serve your app using ngrok
```
ngrok http 5001
```

#### Paste the url provided by ngrok in the Request URL under the Event Subscriptions tab
```
https://api.slack.com/apps/<application-id>/event-subscriptions
```
