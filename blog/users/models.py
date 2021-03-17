from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import os

def get_avatar_path_or_delete_old(instance, filename):
    ext = instance.avatar.url.split('.')[-1]
    path = f"avatar/{instance.id}-{instance.username}.{ext}"
    base_dir = f"{settings.BASE_DIR}{settings.MEDIA_URL}{path}"
    #delete user's avatar If already exists
    if os.path.exists(base_dir):
        os.remove(base_dir)
    return path


class User(AbstractUser):
    job = models.CharField(max_length=255,blank=True)
    avatar = models.ImageField(upload_to=get_avatar_path_or_delete_old,
                                blank=True,null=True)
    url = models.URLField(max_length=120,blank=True)
    telegram = models.CharField(max_length=50,blank=True)
    instagram = models.CharField(max_length=80,blank=True)
    twitter = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.username

