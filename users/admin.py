# coding: utf-8
from django.contrib import admin
from  .models import info

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = info
    can_delete = False
    verbose_name_plural =u'个人资料'
# Define a new User admin
class Useradmin(UserAdmin):
    inlines = (EmployeeInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, Useradmin)
# Register your models here.
