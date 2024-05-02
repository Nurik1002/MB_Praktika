from django import forms
from .models import Category, Post, PostComment
from ckeditor.fields import RichTextFormField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': RichTextFormField(config_name="default"),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }