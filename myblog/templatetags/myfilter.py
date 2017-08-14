#coding:utf-8
from django import template
from myblog import models
from comments.models import Comment,Reply
from users.models import info
register=template.Library()

#获取文章字数
@register.filter(name='GetWordNums')
def GetWordNums(value):
    num = 0
    for i in value:
        if i not in ' \n!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            num = num + 1
    return num

#获取下一页标题
@register.filter(name='Get_Next_Title')
def Get_Next_Title(value):
    try:
        next_title=models.Post.objects.get(id=int(value)+1).title
    except:
        next_title=None
    return next_title
#获取上一页标题
@register.filter(name='Get_Previous_Title')
def Get_Previous_Title(value):
    try:
        previous_title=models.Post.objects.get(id=int(value)-1).title
    except:
        previous_title=None
    return previous_title
#获取评论数
@register.filter(name='Get_Comments_num')
def Get_Comments_num(value):
    try:
        commentnum=Comment.objects.filter(post=value).count()
    except:
        commentnum=0
    return  commentnum

#获取回复
@register.filter(name='Get_Comment_Child')
def Get_Comment_Child(value):
    return Reply.objects.filter(comment=value)
