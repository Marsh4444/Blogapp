from django.urls import path
from django.conf import settings
from bloggApp import views
from . import views

urlpatterns = [
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
]