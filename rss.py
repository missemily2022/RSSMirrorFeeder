import os
import sys
import feedparser
from sql import db
from time import sleep, time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from apscheduler.schedulers.background import BackgroundScheduler


try:
    api_id = int(os.environ["API_ID"])   # Get it from my.telegram.org
    api_hash = os.environ["API_HASH"]   # Get it from my.telegram.org
    feed_urls = list(set(os.environ["FEED_URLS"].split("|")))
    bot_token = os.environ["BOT_TOKEN"]   # Get it by creating a bot on https://t.me/botfather
    log_channel = int(os.environ["LOG_CHANNEL"])   # Telegram Channel ID where the bot is added and have write permission. You can use group ID too.
    check_interval = int(os.environ.get("INTERVAL", 10))   # Check Interval in seconds.  
    max_instances = int(os.environ.get("MAX_INSTANCES", 3))   # Max parallel instance to be used.
    mirr_cmd = os.environ.get("MIRROR_CMD", "/qbmirror")    #if you have changed default cmd of mirror bot, replace this.
except Exception as e:
    print(e)
    print("One or more variables missing or have error. Exiting !")
    sys.exit(1)


for feed_url in feed_urls:
    if db.get_link(feed_url) is None:
        db.update_link(feed_url, "*")


app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def create_feed_checker(feed_url):
    def check_feed():
        FEED = feedparser.parse(feed_url)
        if len(FEED.entries) == 0:
            return
        entry = FEED.entries[0]
        if entry.id != db.get_link(feed_url).link:
                       # ↓ Edit this message as your needs.
            if "eztv.re" in entry.link:   
                message = f"{mirr_cmd} {entry.torrent_magneturi}"
            elif "yts.mx" in entry.link:
                message = f"{mirr_cmd} {entry.links[1]['href']}"
            elif "rarbg" in entry.link:
                message = f"{mirr_cmd} {entry.link}"
            elif "watercache" in entry.link:
                message = f"{mirr_cmd} {entry.link}"
            elif "limetorrents.pro" in entry.link:
                message = f"{mirr_cmd} {entry.link}"
            elif "etorrent.click" in entry.link:
                message = f"{mirr_cmd} {entry.link}"
            else:
                message = f"{mirr_cmd} {entry.link}"
            try:
                msg = app.send_message(log_channel, message)
                db.update_link(feed_url, entry.id)
            except FloodWait as e:
                print(f"FloodWait: {e.x} seconds")
                sleep(e.x)
            except Exception as e:
                print(e)
        else:
            print(f"Checked RSS FEED: {entry.id}")
    return check_feed


scheduler = BackgroundScheduler()
for feed_url in feed_urls:
    feed_checker = create_feed_checker(feed_url)
    scheduler.add_job(feed_checker, "interval", seconds=check_interval, max_instances=max_instances)
scheduler.start()
app.run()
