from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Tracker

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='password')
        testuser1.save()

        testpost = Tracker.objects.create(
            user=testuser1,
            username='Green Eggs and Ham',
            password='I do not like green eggs and ham, Sam I am.',
        )
        testpost.save()

    def test_blog_content(self):
        post = Tracker.objects.get(id=1)
        actual_user = str(post.user)
        actual_username = str(post.username)
        actual_password = str(post.password)
        self.assertEqual(actual_user, 'testuser1')
        self.assertEqual(actual_username, 'Green Eggs and Ham')
        self.assertEqual(actual_password, 'I do not like green eggs and ham, Sam I am.')

