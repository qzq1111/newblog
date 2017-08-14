# coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Comment(models.Model):
    text=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey('myblog.Post')
    user=models.ForeignKey(User)
    def __unicode__(self):
        return self.text[:20]

class Reply(models.Model):
    comment=models.ForeignKey(Comment, related_name='comment_replies')
    form_user=models.ForeignKey(User,related_name='user_comment_replies',null=True,blank=True)#回复用户
    to_user=models.ForeignKey(User,related_name='user_replied',null=True,blank=True)#被回复用户
    body=models.TextField()#回复内容
    created_time=models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return '{0}->{1}'.format(self.form_user, self.to_user)