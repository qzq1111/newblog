from  django.conf.urls import url

from . import  views

app_name='comments'
urlpatterns=[
    url(r'^comment/post/(\d+)/$', views.post_comment, name='post_comment'),
    url(r'^comment/reply/(\w)(\d+)/$',views.reply_comment,name='reply_comment'),
]