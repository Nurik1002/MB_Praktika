from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from users.models import CustomUser
from .models import Post, PostComment




def all_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        if posts:
            data = [
                {
                    "id" : post.id,
                    "title" : post.title,
                    "description" : post.description,
                    "user" : post.user.username,
                    "category_id" : post.category_id
                }
            for post in posts
            ]
            return JsonResponse({"posts": data})
        else:
            return JsonResponse({"error": "Posts not exist"})
    else:
        return JsonResponse({'error': 'Invalid request method.'})
    

def post_detail(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        comments = PostComment.objects.filter(post=post)
        if post:
            data = {
                "id" : post.id,
                "title" : post.title,
                "description" : post.description,
                "user_id" : post.user_id,
                "category_id" : post.category_id,
                "comments" : comments
            }
            return JsonResponse({"post": data})
        else:
            return JsonResponse({"error": "Post not exist"})
    else:
        return JsonResponse({'error': 'Invalid request method.'})

 

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = CustomUser.objects.filter(id = request.user.id)
        category_id = request.POST.get('category_id')
        post = Post(title=title, description=description, user_id=user, category_id=category_id)
        post.save()
        return JsonResponse({"message": "Post created successfully"})
    else:
        return JsonResponse({'error': 'Invalid request method.'})