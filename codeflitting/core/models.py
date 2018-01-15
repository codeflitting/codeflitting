from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        # 定义抽象类,用它来归纳一些公共属性字段
        ordering = ['-last_modified_time']
        abstract = True


class SiteMapModel(models.Model):
    url = models.TextField('url')
