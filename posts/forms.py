import django.forms
from .models import PostCreate
class CreateForm(forms.ModelForm):
    class Meta:
        model = PostCreate
        fields = ['text', 'group']
