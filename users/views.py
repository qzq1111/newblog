# coding:utf-8
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from .import models
from users import forms
# Create your views here.

def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method=="POST":
        form=forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user=User.objects.get(username=request.POST['username'].strip())
            info=models.info(user_id=user.id)
            info.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form=forms.RegisterForm()
    return render(request,'users/register.html',context={'form':form,'next': redirect_to})

def login(request):
    redirect_to = request.POST.get('next',request.GET.get('next', ''))
    if request.method=='POST':
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            login_name=request.POST['username'].strip()
            login_password=request.POST['password']
            user=authenticate(username=login_name,password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request,user)
                    if redirect_to:
                        return redirect(redirect_to)
                    else:
                        return redirect('/')
                else:
                    messages.add_message(request,messages.WARNING,'账户未启用！')
            else:
                messages.add_message(request,messages.WARNING,'账号或密码错误！')
        else:
            messages.add_message(request, messages.WARNING, '账号或密码错误！')
    else:
        form = forms.LoginForm()
    return render(request,'users/login.html',context={'form':form,'next': redirect_to})

@login_required(login_url='/user/login/')
def logout(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    auth.logout(request)
    if redirect_to:
        return redirect(redirect_to)
    else:
        return redirect('/user/login/')

@login_required(login_url='/user/login/')
def change_password(request):

    return

@login_required(login_url='/user/login/')
def information(request):
    if request.method == "POST":
        form=forms.InformationForm(request.POST,request.FILES,instance=request.user)
        print form
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = forms.InformationForm()
        return render(request,'users/information.html',context={'form':form})