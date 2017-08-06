# coding:utf-8
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from .import models
from users import forms
# Create your views here.

def register(request):
    if request.method=="POST":
        form=forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user=User.objects.get(username=request.POST['username'].strip())
            info=models.info(user_id=user.id)
            info.save()
            return redirect('/')
    else:
        form=forms.RegisterForm()
    return render(request,'users/register.html',context={'form':form})
def login(request):
    if request.method=='POST':
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            login_name=request.POST['username'].strip()
            login_password=request.POST['password']
            user=authenticate(username=login_name,password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request,user)
                    return redirect('/')
                else:
                    messages.add_message(request,messages.WARNING,'账户未启用！')
            else:
                messages.add_message(request,messages.WARNING,'账号或密码错误！')
        else:
            messages.add_message(request, messages.WARNING, '账号或密码错误！')
    else:
        form = forms.LoginForm()
    return render(request,'users/login.html',context={'form':form,})

def logout(request):
    auth.logout(request)
    return redirect('/user/login/')

def change_password(request):

    return

def personal_center(request):

    return