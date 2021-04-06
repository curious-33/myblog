from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Post


TOKEN = reverse('user:token')


class PostTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        user1 = get_user_model().objects.create_user(username="TestUser1", password="1234567")
        user1.save()

        post1 = Post.objects.create(title="New post test", content="Hello guys, I'm Curious", author=user1)
        post1.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        payload = {
            'title': f'{post.title}',
            'content': f'{post.content}',
            'author': f'{post.author}'
        }
        res = self.client.post(TOKEN, payload)

        self.assertEqual()
