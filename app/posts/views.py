from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import CommentForm, PostForm
from django.views.decorators.cache import cache_page

@cache_page(3600)
def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts/index.html",context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()

    if request.method == 'POST':
        if request.user.is_authenticated == False:
            return redirect('login')
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post-detail',slug=slug)
    else:
        form = CommentForm()
        
    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, "posts/detail.html",context)

@login_required
def create(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/create.html', {'form': form})
    
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.user = request.user
            post.save()
            # return HttpResponseRedirect(reverse('index'))
            return HttpResponseRedirect(reverse('post-detail', kwargs={'slug': post.slug}))
        
        return render(request, 'posts/create.html', {'form': form})
        
def update(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'GET':
        form = PostForm(initial={'title': post.title, 'content': post.content})
        return render(request, 'posts/update.html', {'form':form, 'post': post})


    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return HttpResponseRedirect(reverse('post-detail', kwargs={'slug': post.slug}))
        
        return render(request, 'posts/update.html', {'form': form, 'post': post})

def delete(request, slug):
    post = get_object_or_404(Post,slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect(reverse(index))
    
    return redirect(reverse('post-detail', kwargs={'slug': post.slug}))