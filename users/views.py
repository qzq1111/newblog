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
            login_name=form.cleaned_data['username']
            login_password=form.cleaned_data['password']
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
    if request.method=="POST":
        form = forms.SetPassWord(request.user,request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '修改成功！')
            return redirect(request.path)
        else:
            messages.add_message(request,messages.WARNING,'检查字段！')
            return redirect(request.path)
    else:
        form =forms.SetPassWord(request.user)
    return render(request,'users/changepassword.html',context={'form':form})

@login_required(login_url='/user/login/')
def information_change(request):
    if request.method == "POST":
        form=forms.InformationForm(request.POST,request.FILES)
        if form.is_valid():
            nikname=form.cleaned_data['nickname']
            qq=form.cleaned_data['qq']
            url=form.cleaned_data['url']
            image=form.cleaned_data['image']
            obj = models.info.objects.get(user_id=request.user)
            obj.nickname=nikname
            obj.qq=qq
            obj.url=url
            if image !='static/images/users/default.png':
                obj.image=image
            obj.save()
            messages.add_message(request,messages.SUCCESS,'修改成功！')
            return redirect(request.path)
        else:
            messages.add_message(request, messages.WARNING, '检查上传图片格式！')
            return redirect(request.path)
    else:
        obj = models.info.objects.get(user_id=request.user)
        form = forms.InformationForm(instance=obj)
        return render(request, 'users/information_change.html', context={'form':form})