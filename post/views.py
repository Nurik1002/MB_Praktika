from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Category, Post, PostComment
from .forms import  CateforyForm, PostForm, PostCommentForm


@login_required(login_url='login')
def post_list(request):
    posts = Post.objects.all()
    context = dict()
    context['posts'] = posts
    return render(request, '', context=context)


@login_required(login_url='login')
def post_detail(request, pk):
    context = dict()
    post = Post.objects.get(id=pk)
    context['post'] = post
    return render(request, '', context=context)
    

@login_required(login_url='login')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            return JsonResponse({'success': True})
    else:
        context = dict()
        form = PostForm()
        context['form'] = form
    return render(request, '', context=context)

@login_required(login_url='login')
def post_comment_list(request):
    pass