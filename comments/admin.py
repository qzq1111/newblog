# coding:utf-8
from django.contrib import admin
from comments import models
# Register your models here.
class Commentadmin(admin.ModelAdmin):
    list_display = ('text','created_time','post','user')
class Replyadmin(admin.ModelAdmin):
    list_display = ('form_user','to_user','body','created_time')
admin.site.register(models.Comment,Commentadmin)
admin.site.register(models.Reply,Replyadmin)