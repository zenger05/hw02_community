from django.urls import path

from .views import *

app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('group/<slug:slug>/', group_posts, name='group_post')
]
