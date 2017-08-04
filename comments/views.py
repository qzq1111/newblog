from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from myblog.models import Post
from .models import Comment
from .forms import CommentForm

def post_comment(request,postid):
    post=get_object_or_404(Post,id=postid)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('/post/'+postid)
        else:
            comment_list=post.comment_set.all().order_by('-created_time')
            context={'post':post,
                     'form':form,
                     'comment_list':comment_list
            }
            return render(request,'post.html',context=context)
    return redirect('/post/'+postid)