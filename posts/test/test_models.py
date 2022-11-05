from django.test import TestCase
from django.contrib.auth import get_user_model

from posts.models import Group, Post

User = get_user_model()


class PostsTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост',
        )

    def test_str_model(self):
        self.assertEqual(self.group.title, str(self.group))

    def test_verbose_name_model(self):
        self.assertEqual(self.post._meta.get_field('group').verbose_name, 'Группа')
        self.assertEqual(self.post._meta.get_field('author').verbose_name, 'Автор')
