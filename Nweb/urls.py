from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path('Maintenance', views.Maintenance, name='Maintenance'),
    path('', views.project_inquiry, name='index'),
    path('inquiry/success/', views.inquiry_success, name='inquiry_success'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('book/', views.book, name='book'),
    path('post_list/', PostListView.as_view(), name='post_list'),  # List all blog posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # View a single blog post
    path('post/new/', PostCreateView.as_view(), name='post_create'),  # Create a new blog post

]
