from django.test import TestCase, Client


class TestAboutUrl(TestCase):

    def setUp(self):
        self.user = Client()

    def test_url_status(self):
        test_url_and_status = {
            '/about/author/': 200,
            '/about/tech/': 200,
        }
        for url, status in test_url_and_status.items():
            with self.subTest(url=url):
                response = self.user.get(url)
                self.assertEqual(response.status_code, status)

    def test_url_template(self):
        test_url_and_template = {
            '/about/author/': 'about/author.html',
            '/about/tech/': 'about/tech.html',
        }
        for url, template in test_url_and_template.items():
            with self.subTest(url=url):
                response = self.user.get(url)
                self.assertTemplateUsed(response, template)