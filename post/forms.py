from django import forms 
from ckeditor.fields import RichTextFormField

from .models import Category, Post, PostComment

class CateforyForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'id':'categoryid', 'placeholder':'placeholder'})
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'id':'categoryid', 'placeholder':'placeholder'}),
            'description': RichTextFormField(config_name="default"),
            'category':forms.Select(attrs={'class':'form-control', 'id':'selectedcategoryid', 'placeholder':'placeholder'}),
        }


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'class':'form-control', 'id':'categoryid', 'placeholder':'placeholder'}),
        }