# -*- coding：utf-8 -*-
from codeflitting.quote.models import Wisdom
import requests
import json
import datetime


def iciba_today_quote():
    dt = datetime.datetime.now().strftime('%Y-%m-%d')
    url = "http://sentence.iciba.com/index.php?callback=jQuery19008964435221647116_1515727016296&c=dailysentence&m=getdetail&title=%s" % dt
    content = requests.get(url).text.replace('jQuery19008964435221647116_1515727016296(', '')[:-1]
    result = json.loads(content)
    english = result.get('content')
    chinese = result.get('note')
    print(english + ' --- ' + chinese + ' --- ' + dt)
    q = Wisdom.objects.get_or_create(english=english)[0]
    q.chinese = chinese
    q.save()


def spider_today_quote():
    print(datetime.datetime.now())
    try:
        iciba_today_quote()
    except Exception as e:
        print(e)
