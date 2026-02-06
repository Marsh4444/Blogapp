from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from blogs.models import Blog, Category
from .forms import CategoryForm

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboards/dashboards.html', context)

def categories(request):
    return render(request, 'dashboards/categories.html')


def add_category(request):
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()

    context = {
        'form': form
    }
    return render(request, 'dashboards/add_category.html', context)