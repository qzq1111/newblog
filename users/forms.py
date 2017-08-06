# coding:utf-8
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

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

class LoginForm(forms.Form):
    username=forms.CharField(label=u'用户名',max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label = u'密码',widget=forms.PasswordInput(attrs={'class':'form-control'}))

#class Personal_center(forms.ModelForm):
 #   class Meta:
  #      model=User
