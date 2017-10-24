from django.db import models
from codeflitting.core.models import BaseModel


class Wisdom(BaseModel):
    author = models.CharField('作者', max_length=50)
    content = models.TextField('格言')
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    tags = models.ManyToManyField('Tag', verbose_name='标签', blank=True)


class Tag(BaseModel):
    name = models.CharField('标签名', max_length=20)

    def __str__(self):
        return self.name


class Joke(BaseModel):
    content = models.TextField('笑话')
