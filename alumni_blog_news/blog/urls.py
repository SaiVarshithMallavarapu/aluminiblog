from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('news/<int:id>/', views.news_detail, name='news_detail'),
    path('add-blog/', views.add_blog, name='add_blog'),
    path('add_news/', views.add_news, name='add_news'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('blog/delete/<int:id>/', views.delete_blog, name='delete_blog'),
    path('news/delete/<int:id>/', views.delete_news, name='delete_news'),
]
