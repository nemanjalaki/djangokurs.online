from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_listing, name='post-list'),
    path('posts/<int:post_id>/', views.post_detail, name='post-detail'),
    path('about-me/', views.about_me, name='about-me'),
    path('', views.homepage, name='homepage'),
    path('add-post', views.add_post, name='add-post'),
]