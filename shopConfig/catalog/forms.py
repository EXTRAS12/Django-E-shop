from django import forms
from .models import Subscriber


class SubForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ['name', 'email']
