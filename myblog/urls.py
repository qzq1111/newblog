from django.conf.urls import url
from myblog import views
app_name='myblog'
urlpatterns = [
    url(r'^$',views.index,name='index_url'),
    url(r'^post/(\d+)/$',views.post,name='post_url'),
    url(r'^category/(\w+)/$',views.category,name='category_url'),
    url(r'^search/$',views.search,name='search_url'),
]