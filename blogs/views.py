from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category

# Create your views here.

def posts_by_category(request, category_id):

#THis gets all
    posts = Blog.objects.filter(category=category_id, status='published').order_by('updated_at')
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except Category.DoesNotExist:
    #     return redirect('home')

#This gets one
    category = get_object_or_404(Category, pk=category_id)
            
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'category.html', context)

def blogs(request, blog_slug):
    single_post = get_object_or_404(Blog, slug=blog_slug, status='published')
    context = {
        'single_post':single_post
    }
    return render(request, 'blogs.html', context)