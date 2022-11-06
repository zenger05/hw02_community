from django.test import Client
from unittest import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class UserUrlTest(TestCase):

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='Pozhalusta')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_url_status_code(self):
        test_status_and_urls = {
            '/auth/signup/': 200,
            '/auth/logout/': 302,
            '/auth/login/': 200,
            '/auth/password_change/': 200,
            '/auth/password_change/done/': 200,
            '/auth/password_reset/': 200,
            '/auth/password_reset/done/': 200,
        }
        for url, status in test_status_and_urls.items():
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                self.assertEqual(response.status_code, status)

    def test_url_client(self):
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
