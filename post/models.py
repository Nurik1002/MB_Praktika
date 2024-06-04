from django.db import models
from ckeditor.fields import RichTextField
from user.models import CustomUser



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")

    def __str__(self) -> str:
        return  f"{self.name}"
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "1. Categories"


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    description = RichTextField(null=True, blank=True,     config_name="default")
    author = models.ForeignKey(CustomUser, verbose_name="Author", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created time")

    def __str__(self) -> str:
        return  f"{self.author.username} {self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "2. Posts"

class PostComment(models.Model):
    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
    comment = models.CharField(max_length=1024, verbose_name="Comment")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created time")

    def __str__(self) -> str:
        return  f"{self.post.title} {self.comment}"
    
    class Meta:
        verbose_name = "Post Comment"
        verbose_name_plural = "3. Post Comments"