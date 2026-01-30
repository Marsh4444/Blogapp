from django.shortcuts import render

from .models import Blog

# Create your views here.

def posts_by_category(request, category_id):

    posts = Blog.objects.filter(category=category_id, status='published').order_by('updated_at')
    context = {
        'posts': posts
    }
    return render(request, 'category.html', context)