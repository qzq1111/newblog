#coding:utf-8
from myblog import models
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import re

def recommend():
    recommend = models.Post.objects.all().order_by('-views')[0:10]  # 推荐阅读功能
    return recommend
#目录功能
def find_id(value):
    alls=re.findall("<h2 id='(.+)'|<h3 id='(.+)'",value)
    list_id=[]
    for p in alls:
        if p[0]:
            list_id.append(p[0])
        else:
            list_id.append(p[1])
    return list_id
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