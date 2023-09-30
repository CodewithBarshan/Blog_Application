from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Category
# Create your views here.

def home(request):
    all_post=Post.objects.all()
    cats=Category.objects.all()
    return render (request,'blog/home.html',{'all_post':all_post,'cats':cats})

def post_detail(request,url):
    post = get_object_or_404(Post, url=url)
    cats=Category.objects.all()
    return render(request, 'blog/post_detail.html',{'post':post,'cats':cats})

def category_detail(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,'blog/cat_post.html',{'cat':cat,'posts':posts})

def about(request):
    return render(request,"blog/about.html")