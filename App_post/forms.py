from django import forms 
from App_post.models import Post


class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']