from django.db import models
from codeflitting.core.models import BaseModel


class Wisdom(BaseModel):
    english = models.TextField('格言-英文')
    chinese = models.TextField('格言-中文')
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    author = models.ForeignKey('Author', verbose_name='作者', blank=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', verbose_name='标签', blank=True)


class Author(BaseModel):
    name = models.CharField('作者', max_length=50)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField('标签名', max_length=20)

    def __str__(self):
        return self.name


class Navbar(BaseModel):
    order = models.PositiveIntegerField('顺序', default=0)
    name = models.CharField("导航名", max_length=20)
    icon = models.CharField("图标", max_length=20)
    href = models.CharField("地址", max_length=20)


class Joke(BaseModel):
    content = models.TextField('笑话')
