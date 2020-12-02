from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    #model=Post
    #fields=['title','content','status','post_author']
    class Meta:
        model=Post
        fields=['title','content']



