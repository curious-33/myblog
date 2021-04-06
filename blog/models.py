from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    subtitle = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey('user.User', related_name='posts', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now)
    date_updated = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.title} - {self.author}'

