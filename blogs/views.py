from django.shortcuts import get_object_or_404, render

from .models import Blog, Category

# Create your views here.

def posts_by_category(request, category_id):

    posts = Blog.objects.filter(category=category_id, status='published').order_by('updated_at')
        # try:
        #     category = Category.objects.get(pk=category_id)
        # except Category.DoesNotExist:
        #     category = "Unknown Category"
    category = get_object_or_404(Category, pk=category_id)
            
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'category.html', context)