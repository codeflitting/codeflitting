# -*- coding：utf-8 -*-
from codeflitting.quote.models import Wisdom, Author, Topic
import requests
import json
import datetime
from bs4 import BeautifulSoup


def insert_database(chinese, english, author="", topic=""):
    wisdom = Wisdom.objects.get_or_create(english=english)[0]
    wisdom.chinese = chinese
    if author != '':
        author = Author.objects.get_or_create(name=author)[0]
        wisdom.author = author
    if topic != '':
        topic = Topic.objects.get_or_create(name=topic)[0]
        wisdom.topic = topic
    wisdom.save()


def iciba_today_quote():
    dt = datetime.datetime.now().strftime('%Y-%m-%d')
    url = "http://sentence.iciba.com/index.php?callback=jQuery19008964435221647116_1515727016296&c=dailysentence&m=getdetail&title=%s" % dt
    content = requests.get(url).text.replace('jQuery19008964435221647116_1515727016296(', '')[:-1]
    result = json.loads(content)
    english = result.get('content')
    chinese = result.get('note')
    print(english + ' --- ' + chinese + ' --- ' + dt)
    insert_database(chinese, english)


def brainyquote_today_quote():
    url = "https://www.brainyquote.com/quote_of_the_day"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    for divs in soup.find_all('div', {'class': 'container bqQOTD'}):
        for div in divs.find_all('div', {'class': 'm-brick grid-item boxy bqQt'}):
            topic = div.find_all('h2', {'class': 'qotd-h2'})[0].text.strip()
            author = div.find_all('a', {'class': 'bq-aut'})[0].text.strip()
            if len(topic) > 17:
                topic = topic.split(' ')[0]
            else:
                topic = ''
            english = div.find_all('a', {'class': 'b-qt'})[0].text.strip()
            print(english + ' --- ' + topic + ' --- ' + author)
            insert_database('', english, author, topic)


def spider_today_quote():
    print(datetime.datetime.now())
    try:
        iciba_today_quote()
    except Exception as e:
        print(e)

    try:
        brainyquote_today_quote()
    except Exception as e:
        print(e)
