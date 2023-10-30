from django.shortcuts import render, get_object_or_404
from .models import Category, Post

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts":posts})

def category(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {"category": category})