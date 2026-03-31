from django import forms
from .models import Post, Reply 

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'photo'] 

class ReplyForm(forms.ModelForm):
    class Meta: 
        model = Reply 
        fields = ['content']