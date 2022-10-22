from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        'password_change/',
        views.MyPasswordChangeView.as_view(),
        name='change_password'

    ),
    path(
        'password_change/done/',
        views.MyPasswordResetDoneView.as_view(),
        name='change_password_done'
    ),
    path(
        'password_reset/',
        views.MyPasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'reset/<uidb64>/<token>/',
        views.MyPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        views.MyPasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
    path(
        'password_reset/done/',
        views.MyPasswordResetEmailDoneView.as_view(),
        name='password_done'
    )

]