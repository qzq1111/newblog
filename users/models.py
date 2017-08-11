from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class info(models.Model):
    nickname=models.CharField(max_length=10,blank=True)
    qq=models.CharField(max_length=15,blank=True,null=True)
    url=models.URLField(max_length=200,blank=True,null=True)
    image=models.ImageField(upload_to='static/images/users/%Y/%m',
                            default='static/images/users/default.png',
                            max_length=200,blank=True,null=True)
    user=models.OneToOneField(User)
    def __unicode__(self):
        return self.nickname

