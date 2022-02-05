FROM ghcr.io/missemily2022/rssbot:feeder

WORKDIR /app
RUN chmod 777 /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3","rss.py"]