from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog, News
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

def home(request):
    blogs = Blog.objects.all().order_by('-created_at')
    news = News.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'blogs': blogs, 'news': news})

def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog_detail.html', {'blog': blog})

def news_detail(request, id):
    news_item = News.objects.get(id=id)
    return render(request, 'news_detail.html', {'news': news_item})

@login_required
def add_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')  # Get the uploaded image

        blog = Blog(title=title, content=content, author=request.user, image=image)
        blog.save()
        return redirect('home')
    
    return render(request, 'add_blog.html')
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def add_news(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')  # Get the uploaded image

        news = News(title=title, content=content, author=request.user, image=image)
        news.save()
        return redirect('home')
    
    return render(request, 'add_news.html')

def logout_view(request):
    logout(request)
    return redirect('home') 

@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if blog.author == request.user:
        blog.delete()
    return redirect('home')

@login_required
def delete_news(request, id):
    news_item = get_object_or_404(News, id=id)
    if news_item.author == request.user:
        news_item.delete()
    return redirect('home')