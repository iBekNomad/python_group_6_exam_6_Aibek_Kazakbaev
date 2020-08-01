from django import forms
from .models import STATUS_CHOICES


default_status = STATUS_CHOICES[0][0]
BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


class GuestBookForm(forms.Form):
    name = forms.CharField(max_length=40, required=True, label='Гость')
    email = forms.EmailField(max_length=30, required=True, label='Электронная почта')
    text = forms.CharField(max_length=2000, required=True, label='Текст')
    # status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Статус',
    #                            initial=default_status)
    # created_at = forms.DateTimeField(required=False, label='Время создания',
    #                                  input_formats=['%Y-%m-%d', BROWSER_DATETIME_FORMAT,
    #                                                 '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
    #                                                 '%Y-%m-%d %H:%M:%S'],
    #                                  widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
