# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from myblog.models import Post
from comments.models import Comment, Reply
from .forms import CommentForm, ReplyCommentForm


@login_required(login_url='/user/login/')
def post_comment(request, postid):
    post = get_object_or_404(Post, id=postid)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = User.objects.get(id=request.user.id)
            comment.save()
            return redirect('/post/' + postid)
        else:
            comment_list = post.comment_set.all().order_by('-created_time')
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'post.html', context=context)
    return redirect('/post/' + postid)


@login_required(login_url='/user/login/')
def reply_comment(request, logo, id):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = ReplyCommentForm(request.POST)
        form_user = request.POST['form_user']
        to_user = request.POST['to_user']
        comments = request.POST['comment']
        if form.is_valid():
            reply = Reply()
            reply.comment_id = comments
            reply.to_user_id = to_user
            reply.form_user_id = form_user
            reply.body = form.cleaned_data['body']
            reply.save()
            return redirect(redirect_to)
        else:
            messages.add_message(request,messages.WARNING,'检查你的字段~~')
            return redirect(request.path)
    else:
        if logo == 'c':  # f代表主评论，r代表回复
            comment = get_object_or_404(Comment, id=id)
        elif logo == 'r':
            comment = get_object_or_404(Reply, id=id)
        else:
            return HttpResponse(status=404)
        form = ReplyCommentForm()
    return render(request, 'comments/reply_comment.html',
                  context={'form': form, 'comment': comment, 'next': redirect_to,})
