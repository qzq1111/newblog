from django.contrib import admin

# Register your models here.
from  myblog import models

class Postadmin(admin.ModelAdmin):
    list_display = ('title','created_time','modified_time','author')
    ordering = ('-created_time',)
class Sortadmin(admin.ModelAdmin):
    list_display = ('name',)
class Tagadmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(models.Post,Postadmin)
admin.site.register(models.Sort,Sortadmin)
admin.site.register(models.Tag,Tagadmin)