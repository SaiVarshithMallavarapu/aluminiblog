# Generated by Django 5.1 on 2024-08-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='media/blog_images/Indian_Institute_of_Technology,_Indore_Logo.png', upload_to='blog_images/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default='media/blog_images/Indian_Institute_of_Technology,_Indore_Logo.png', upload_to='news_images/'),
        ),
    ]
