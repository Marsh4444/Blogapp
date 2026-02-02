
from django.shortcuts import render
from blogs.models import  Blog
from assignment.models import About 

def home(request):
    featured_posts = Blog.objects.filter( is_featured = True, status='published').order_by('-updated_at')
    blogs = Blog.objects.filter(is_featured=False, status='published').order_by('-updated_at')

    try:
        about_info = About.objects.get()
    except About.DoesNotExist:
        about_info = None
    
    

    context= {
        "featured_posts" : featured_posts,
        "blogs" : blogs,
        "about_info": about_info,
        
    }
 
    return render(request, 'home.html', context)