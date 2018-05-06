from codeflitting.quote.models import Author, Wisdom, Tag, Topic
from django.utils import timezone
import time, datetime


def get_tag_set(s):
    result = set()
    if s == '':
        return result
    for tag_name in s.split(','):
        t = Tag.objects.get_or_create(name=tag_name)
        result.add(t[0])
    return result


def get_wisdom(s1, s2):
    if s1 == '':
        return Wisdom.objects.get_or_create(chinese=s2)[0]
    if s2 == '':
        return Wisdom.objects.get_or_create(english=s1)[0]

    try:
        w = Wisdom.objects.get(english=s1)
        w.chinese = s2
        return w
    except:
        pass

    try:
        w = Wisdom.objects.get(chinese=s2)
        w.english = s1
        return w
    except:
        pass

    return Wisdom.objects.create(english=s1, chinese=s2)


def get_strptime(str1):
    strptime = time.mktime(time.strptime(str1, '%Y-%m-%d'))
    return strptime


def get_datetime(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return dt


def insert_data(file_path):
    with open(file_path) as f:
        for line in f.readlines():
            line = line.strip('\n')
            english, chinese, author, topic, tags, created_time = line.split('###')[:6]
            wisdom = get_wisdom(english, chinese)
            if author == '':
                author = '佚名'
            author = Author.objects.get_or_create(name=author)[0]
            wisdom.author = author

            if topic != '':
                topic = Topic.objects.get_or_create(name=topic)[0]
                wisdom.topic = topic
            print(created_time)
            if created_time != '':
                dt = get_datetime(get_strptime(created_time))
                wisdom.last_modified_time = dt
                wisdom.save()
                wisdom.created_time = dt
                wisdom.save()
            tags = get_tag_set(tags)
            if len(tags) > 0:
                wisdom.tags.set(tags)
            wisdom.save()
