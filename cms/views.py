from django.shortcuts import render
from .models import Author, Post, Comment
from .forms import PostForm

def post_listing(request):
    """A view of all posts."""
    posts = Post.objects.all()
    return render(request, 'cms/post_listing.html', {'posts': posts})

def post_detail(request, post_id):
    """A view of all posts."""
    post = Post.objects.get(pk=post_id)
    try:
        comments = Comment.objects.all()
    except Comment.DoesNotExist:
        comments = "There are no comments on this"
    # comment = Comment.objects.filter(pk=post_id)
    return render(request, 'cms/post_detail.html', {'post': post, 'comments':comments})

def homepage(request):
    return render(request, 'cms/homepage.html', {})

def about_me(request):
    return render(request, 'cms/about.html', {})

def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'cms/add-post.html', {'form':form})