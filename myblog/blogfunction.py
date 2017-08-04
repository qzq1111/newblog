#coding:utf-8
from myblog import models
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import re

def recommend():
    recommend = models.Post.objects.all().order_by('-views')[0:10]  # 推荐阅读功能
    return recommend
#分页功能
def page_all(value):
    post = models.Post.objects.all() # 所以文章
    paginator=Paginator(post,1)
    page=value
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return posts