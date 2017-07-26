#coding:utf-8
from django import template

register=template.Library()

@register.filter(name='GetWordNums')
def GetWordNums(value):
    num = 0
    for i in value:
        if i not in ' \n!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            num = num + 1
    return num



