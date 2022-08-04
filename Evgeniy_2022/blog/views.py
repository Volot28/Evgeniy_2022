from django.shortcuts import render
from . models import Post
# Create your views here.

def blog_index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'blog_index.html', context)

def blog_detail(request, pk):
    post=Post.objects.get(pk=pk)
    context={
        'post':post
    }
    return render(request,'blog_detail.html',context)
