from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Category, Post, PostComment
from .forms import  CateforyForm, PostForm, PostCommentForm



@login_required(login_url='login')
def post_detail(request, pk):
    context = dict()
    post = Post.objects.get(id=pk)
    context['post'] = post
    return render(request, 'post/post_detail.html', context=context)
    

@login_required(login_url='login')
def post_create(request):
    context = dict()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return JsonResponse({'success': True})
    else:
        
        form = PostForm()
        context['form'] = form
    return render(request, 'post/create_post.html', context=context)

@login_required(login_url='login')
def post_comment_list(request):
    pass