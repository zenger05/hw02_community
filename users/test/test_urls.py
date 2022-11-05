from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from posts.models import Post, Group

User = get_user_model()


class TestUsersUrl(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()
        cls.user = User.objects.create_user(username='Zenger1')
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.user)

    def test_url_status_code(self):
        test_url_status = {
            '/auth/signup/': 200,
            '/auth/logout/': 302,
            '/auth/login/': 200,
            '/auth/password_change/': 200,
            '/auth/password_change/done/': 200,
            '/auth/password_reset/': 200,
            '/auth/password_reset/done/': 200,
        }

        for url, status in test_url_status.items():
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                self.assertEqual(response.status_code, status)

        test_url_status_2 = {
            '/auth/signup/': 200,
            '/auth/logout/': 302,
            '/auth/login/': 200,
            '/auth/password_change/': 302,
            '/auth/password_change/done/': 200,
            '/auth/password_reset/': 200,
            '/auth/password_reset/done/': 200,
        }

        for url, status in test_url_status_2.items():
            with self.subTest(url=url):
                response = self.guest_client.get(url)
                self.assertEqual(response.status_code, status)
