from django import forms
from comments.models import Comment,Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']
        widgets={
            'text':forms.Textarea(attrs={'class':'form-control'})
        }
class ReplyCommentForm(forms.ModelForm):
    class Meta:
        model=Reply
        fields=['body']
        widgets={
            'body':forms.Textarea(attrs={'class':'form-control'})
        }