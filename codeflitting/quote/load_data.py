from codeflitting.quote.models import Author, Wisdom, Tag

# english----chinese----tag1,tag2----author
def get_tag_set(s):
    result = set()
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


def insert_data(file_path):
    with open(file_path) as f:
        for line in f.readlines():
            line = line.strip('\n')
            english, chinese, tags, author = line.split('----')
            tags = get_tag_set(tags)
            wisdom = get_wisdom(english, chinese)
            author = Author.objects.get_or_create(name=author)[0]
            wisdom.author = author
            wisdom.save()
            wisdom.tags.set(tags)
