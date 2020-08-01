from django import forms
from .models import STATUS_CHOICES


default_status = STATUS_CHOICES[0][0]
BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


class GuestBookForm(forms.Form):
    name = forms.CharField(max_length=40, required=True, label='Гость')
    email = forms.EmailField(max_length=30, required=True, label='Электронная почта')
    text = forms.CharField(max_length=2000, required=True, label='Текст')
