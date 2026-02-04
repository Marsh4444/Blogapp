
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from .forms import RegistrationForm
from blogs.models import  Blog
from assignment.models import About 
from django.contrib import messages, auth

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

class StyledRegistrationForm(RegistrationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})



def register(request):
    if request.method == "POST":
        form = StyledRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print(form.errors)  # Debugging line to see form errors
    else:
        form = StyledRegistrationForm()

    context = {"form": form}

    return render(request, "register.html", context)


def login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: # checks if user exists
            auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")
        
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("home")   # or "login"