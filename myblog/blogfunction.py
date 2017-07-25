#coding:utf-8
from myblog import models

def recommend():
    recommend = models.Post.objects.all().order_by('-views')[0:10]  # 推荐阅读功能
    return recommend