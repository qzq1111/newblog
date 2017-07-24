#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#标签
class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
#分类
class Sort(models.Model):
    name=models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
#博文
class Post(models.Model):
    '''
    1.题目2.主体内容3.创建时间4.最后一次修改时间5.摘要6.分类 7.标签8.作者
    '''
    title=models.CharField(max_length=50)
    body=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    modified_time=models.DateTimeField()
    summary=models.CharField(max_length=100,blank=True)
    sort=models.ForeignKey(Sort)
    tags=models.ManyToManyField(Tag,blank=True)
    author=models.ForeignKey(User)
    def __unicode__(self):
        return self.title
