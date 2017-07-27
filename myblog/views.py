#coding:utf-8
import markdown
from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from myblog import models
from myblog import blogfunction
# Create your views here.


#主页
def index(request):
    post=models.Post.objects.all().order_by('created_time')#所以文章
    recommend=blogfunction.recommend()#推荐
    categorys=models.Category.objects.all()#类别
    paginator=Paginator(post,5)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(request,'index.html',context={'posts':posts,'categorys':categorys,'recommend':recommend,})
#显示具体文章
def post(request,postid):
    try:
        post=models.Post.objects.get(id=postid)
        post.update_views()
        post.body=markdown.markdown(post.body,extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',])
        tags=post.tags.all()
        contents=blogfunction.find_id(post.body)#目录
        posts=blogfunction.page_all(postid)#当前文章页数
    except:
        return redirect('/')
    return render(request,'post.html',context={'post':post,'tags':tags,'contents':contents,'posts':posts})
#类别功能
def category(request,categoryname):
    try:
        category=models.Category.objects.get(name=categoryname)
        posts=models.Post.objects.filter(category=category)
        categorys=models.Category.objects.all()
    except:
        return  redirect('/')
    return render(request, 'category.html', context={'posts':posts, 'category':category,'categorys':categorys})
#搜索功能
def search(request):
    title=request.GET.get('title')
    titles=models.Post.objects.filter(title__contains=title)
    recommend = blogfunction.recommend()
    return render(request,'search.html',context={'titles':titles,'recommend':recommend,})


