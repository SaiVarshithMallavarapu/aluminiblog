from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', default='/blog_images/Indian_Institute_of_Technology,_Indore_Logo.png')

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/',  default='/news_images/Indian_Institute_of_Technology,_Indore_Logo.png')  

    def __str__(self):
        return self.title
