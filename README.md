# RSSMirrorFeeder Telegram Bot
A bot to post messages to Telegram Groups or Channels from rss feed.
- This bot can also send /qbmirror commands to your mirror bot 
bcoz bot can't read another bot's mag. So this bot will use your TG account to interact with mirror bot.
Fill `MIRROR_CHAT_ID` var to enable it.

## Configuration
- Edit the [rss.py](./rss.py) as your needs.
- Edit values in [config.env](./config.env.template) or set it in Environment Variables. There is an template for `config.env` already exists just edit it and rename the file.

### Configuration Values
- `APP_ID` - Get it from [my.telegram.org](https://my.telegram.org/apps)
- `API_HASH` - Get it from [my.telegram.org](https://my.telegram.org/apps)
- `BOT_TOKEN` - Get it by creating a Telegram bot on [BotFather](https://t.me/BotFather)
- `FEED_URLS` - List of URLs of RSS Feed, sperated by `|` vertical bar.
- `LOG_CHAT` - ID of the Telegram Chat where messages are to be posted.
- `DATABASE_URL` - Here is a full [guide](https://github.com/SpEcHiDe/NoPMsBot/wiki/How-to-Install-Database-%3F). For Heroku, just add the `Heroku Postgres` add-on.
- `INTERVAL` - Checking Interval in seconds. (optional)
- `MAX_INSTANCES` - Max instances to be used while checking rss feed. (optional)
### Working as a userbot on your behalf to interact with mirror bot.

These variabls are required only if you want to use your tg account to send /mirror cmd to any mirror bot.
- `MIRROR_CHAT_ID` - Group/chat_id of mirror chat or mirror bot to send mirror cmd.
- `MIRROR_CMD` - if you have changed default cmd of mirror bot, replace this.

## Deployment

### Deploying on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/missemily2022/RSSMirrorFeeder)

### VPS or any other server/pc

- Install requirements from [requirements.txt](./requirements.txt)
```
pip3 install -r requirements.txt
```
- Deploy
```
python3 rss.py
```

# How to Setup Auto RSS Mirror Group

1. Create Channel (Add your bot to your channel, automatically as admin )
2. in Channel > Manage Channel > then Linked your group
3. Add Bot to your group (as admin)
4. in config.env MIRROR_CHAT_ID fill with channel ID (not group ID)

<b>Use this along with [RSSMirrorBot](https://github.com/missemily2022/RSSMirrorBot) to use RSS Auto Mirror</b>

<b><i>Credits: </i></b>[Miss Emily](https://t.me/missemily2022)


