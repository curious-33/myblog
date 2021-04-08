from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default="programming")
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'Title: {self.title} \n Author: {self.author}'


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
