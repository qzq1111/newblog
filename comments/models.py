from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Comment(models.Model):
    text=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey('myblog.Post')
    user=models.ForeignKey(User)
    def __str__(self):
        return self.text[:20]
