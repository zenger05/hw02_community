from django.shortcuts import render


from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:change_password_done')


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_change_done.html'

#@method_decorator(login_required, name='dispatch')
class MyPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    success_url = reverse_lazy('users:password_done')
    send_mail('The contact subject', 'This is the message', 'bret91@hotmail.com', [])


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/users/password_reset_complete.html'

class MyPasswordResetEmailDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_email_done.html'








