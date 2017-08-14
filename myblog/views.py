#coding:utf-8
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from comments.forms import CommentForm
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
    post=get_object_or_404(models.Post,id=postid)
    post.update_views()#更新浏览次数
    md=markdown.Markdown(extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                        TocExtension(slugify=slugify),])
    post.body=md.convert(post.body)#生成目录
    tags=post.tags.all()#标签
    post_top_back=blogfunction.page_all(postid)#当前文章页数,前后文章
    form =CommentForm()#评论表单
    comment_list=post.comment_set.all().order_by('-created_time')
    return render(request,'post.html',context={'post':post,'tags':tags,
                                               'post_top_back':post_top_back,
                                               'form':form,'comment_list':comment_list,'toc':md.toc})
#类别功能
def category(request,categoryname):
    category=get_object_or_404(models.Category,name=categoryname)
    posts=models.Post.objects.filter(category=category)
    categorys=models.Category.objects.all()
    return render(request, 'category.html', context={'posts':posts, 'category':category,'categorys':categorys})
#搜索功能
def search(request):
    title=request.GET.get('title')
    titles=models.Post.objects.filter(title__contains=title)
    recommend = blogfunction.recommend()
    return render(request,'search.html',context={'titles':titles,'recommend':recommend,})
