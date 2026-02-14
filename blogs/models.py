from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.category_name


STATUS_CHOICES = (
    ("drafted", "Drafted"),
    ("published", "Published")
)
    

class Blog(models.Model):
    """Blog table, contains all the fields required for creating a Blog Table"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_desc = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="drafted")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment table, contains all the fields required for creating a Comment Table"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog.title}"



    

