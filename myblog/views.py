#coding:utf-8
import markdown
from django.shortcuts import render
from myblog import models
# Create your views here.


def index(request):
    posts=models.Post.objects.all()
    sorts=models.Sort.objects.all()
    return render(request,'index.html',context={'posts':posts,'sorts':sorts})
def post(request,postid):
    try:
        post=models.Post.objects.get(id=postid)
        post.body=markdown.markdown(post.body,extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',])
        tags=post.tags.all()
    except:
        post=None
        tags=None
    return render(request,'post.html',context={'post':post,'tags':tags})
def sorts(request,sortid):
    sort=models.Sort.objects.get(id=sortid)
    posts=models.Post.objects.filter(sort=sort)
    return render(request,'sort.html',context={'posts':posts})