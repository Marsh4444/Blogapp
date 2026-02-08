from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from blogs.models import Blog, Category
from .forms import BlogPostForm, CategoryForm
from django.template.defaultfilters import slugify

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

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.category_name = request.POST['category']
        category.save()
        return redirect('categories')
    
    
    context = {
        'category': category
    }
    return render(request, 'dashboards/edit_category.html', context)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')


def posts(request):
    posts = Blog.objects.all().order_by('-created_at')

    context = {
        'posts': posts
    }
    return render(request, 'dashboards/posts.html', context)


def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) #temporarily save the form data to a post object without committing to the database
            post.author = request.user #set the author field of the post to the currently logged-in
            post.save()
            title = form.cleaned_data['title'] #get the title field from the cleaned form data
            post.slug = slugify(post.title) + '-' + str(post.id) #generate a slug from the post title and assign it to the slug field of the post
            post.save() #save the post object to the database with the updated slug field
            return redirect('posts')
        else:
            print('Form is not valid:')
            print(form.errors)
    else:
        form = BlogPostForm()

    context = {
        'form': form
    }
    return render(request, 'dashboards/add_post.html', context)


def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'dashboards/edit_post.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')