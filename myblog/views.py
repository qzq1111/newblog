#coding:utf-8
import markdown
from django.shortcuts import render,redirect

from myblog import models
# Create your views here.


def index(request):
    posts=models.Post.objects.all()
    sorts=models.Sort.objects.all()
    return render(request,'index.html',context={'posts':posts,'sorts':sorts})
def post(request,postid):
    try:
        post=models.Post.objects.get(id=postid)
        post.update_views()
        post.body=markdown.markdown(post.body,extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',])
        tags=post.tags.all()
    except:
        return redirect('/')
    return render(request,'post.html',context={'post':post,'tags':tags})
def sorts(request,sortid):
    try:
        sort=models.Sort.objects.get(id=sortid)
        posts=models.Post.objects.filter(sort=sort)
        print  posts
    except:
        return  redirect('/')
    return render(request,'sort.html',context={'posts':posts,'sort':sort,})

def search(request):
    title=request.GET['title']
    titles=models.Post.objects.filter(title__contains=title)
    return render(request,'search.html',context={'titles':titles})
