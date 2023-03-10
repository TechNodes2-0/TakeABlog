from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255, null=False)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null =True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='thumbnail/', blank = False, null =False)
    category = models.CharField(max_length=255, default = 'uncategorized')
    likes = models.ManyToManyField(User, related_name="blog_post")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.title) + ' | ' + str(self.author) + ' | ' + str(self.title_tag)

    def get_absolute_url(self):
        return reverse('home')
