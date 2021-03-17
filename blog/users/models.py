from django.db import models
from django.contrib.auth.models import AbstractUser

def get_avatar_path_name(instance, filename):
    path = 'media/avatar/'
    name = str(instance.id) + "-" + instance.username
    path = path + name
    return path


class User(AbstractUser):
    job = models.CharField(max_length=100,blank=True)
    avatar = models.ImageField(upload_to=get_avatar_path_name, blank=True, 
                                null=True)
    url = models.URLField(max_length=100,blank=True)
    telegram = models.CharField(max_length=32,blank=True)
    instagram = models.CharField(max_length=30,blank=True)
    twitter = models.CharField(max_length=15,blank=True)

    def __str__(self):
        return self.username

