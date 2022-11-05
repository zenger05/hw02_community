from django.forms import ModelForm

from .models import Post


class CreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group']

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['group'].empty_label = None
        #following line needed to refresh widget copy of choice list
        self.fields['group'].widget.choices = self.fields['group'].choices

