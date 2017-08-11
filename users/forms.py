# coding:utf-8
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm
from django.contrib.auth.models import User
from users.models import info
from django import forms

#注册表单
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email')
        widgets={'username':forms.TextInput(attrs={'class':'form-control',}),
                 'email':forms.EmailInput(attrs={'class':'form-control',}),
                 }
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
#登陆表单
class LoginForm(forms.Form):
    username=forms.CharField(label=u'用户名',max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label = u'密码',widget=forms.PasswordInput(attrs={'class':'form-control'}))

#个人信息表单
class InformationForm(forms.ModelForm):
   class Meta:
        model=info
        fields=['nickname','qq','url','image']
        widgets={'nickname':forms.TextInput(attrs={'class':'form-control',}),
                 'qq':forms.TextInput(attrs={'class':'form-control',}),
                 'url':forms.URLInput(attrs={'class':'form-control',}),
                 'image':forms.FileInput(attrs={'class':'btn',})
                 }
        labels={'nickname':u'昵称',
                'qq':u'QQ',
                'url':u'个人网址',
                'image':u'上传头像',
        }
        help_texts={
            'nickname':u'最多可输入10个汉字',
        }
#修改密码表单
class SetPassWord(SetPasswordForm):
    def __init__(self,*args, **kwargs):
        super(SetPassWord,self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
