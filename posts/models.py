from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Группа',
    )

    def __str__(self):
        return self.text[:15]

    def get_absolute_url(self):
        return f'/posts/{self.pk}/'


class Group(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
