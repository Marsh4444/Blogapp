from webbrowser import get
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from .models import Blog, Category, Comment
from django.contrib.auth.decorators import login_required

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
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_post
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    #This gets all the comments for a single post
    comments = Comment.objects.filter(blog=single_post)
    comments_count = comments.count()
    context = {
        'single_post':single_post,
        'comments': comments,
        'comments_count': comments_count,
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_desc__icontains=keyword) | Q(blog_body__icontains=keyword), status='published').order_by('-updated_at')

    context = {
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html', context)
