import os
from django.conf import settings
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


User = get_user_model()


# class Tag(models.Model):
#     title = models.CharField(max_length=255, unique=True)
#
#     def __str__(self):
#         return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True, default="")
    slug = models.CharField(max_length=100, default="")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ['name']

    def __str__(self):
        return self.name


def place_thumbnail(instance, filename):
    counter = 1
    ext = instance.thumbnail.url.split('.')[-1]
    path = f'thumbnail/{instance.category}-{instance.title}.{ext}'
    base_dir = f'{settings.BASE_DIR}{settings.MEDIA_URL}{path}'

    if os.path.exists(base_dir):
        path = f'thumbnail/{instance.category}-{instance.title}-{instance.published_at}.{ext}'
        counter += 1
    return path


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=place_thumbnail, null=True, blank=True)
    content = RichTextField(null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    views = models.IntegerField(default=0, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, editable=False)
    published_at = models.DateTimeField(default=datetime.now, editable=False)
    is_published = models.BooleanField(default=False, verbose_name="Is published")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_at']

    def publish(self):
        self.is_published = True
        self.published_at = datetime.now()
        self.save()

    def __str__(self):
        return f'Title: {self.title} \n Author: {self.author}'


