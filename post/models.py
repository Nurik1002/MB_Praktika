from django.db import models
from ckeditor.fields import RichTextField
from users.models import CustomUser



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")

    def __str__(self) -> str:
        return  f"{self.name}"
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "1. Categories"


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    category = RichTextField(null=True, blank=True, 
    config_name="special", external_plugin_resources=[(
    'youtube', '/static/shareledge/ckeditor-plugins/youtube/youtube/', 'plugin.js',
    )])
    author = models.ForeignKey(CustomUser, verbose_name="Author", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created time")

    def __str__(self) -> str:
        return  f"{self.author.username} {self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "2. Posts"

class PostComment(models.Model):
    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
    comment = models.CharField(max_length=1024, verbose_name="Comment")

    def __str__(self) -> str:
        return  f"{self.post.title} {self.comment}"
    
    class Meta:
        verbose_name = "Post Comment"
        verbose_name_plural = "3. Post Comments"