from django.db import models
from django.utils import timezone


STATUS_CHOICES = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
]


class GuestBook(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False, verbose_name='Гость')
    email = models.EmailField(max_length=30, null=False, blank=False, verbose_name='Электронная почта')
    text = models.CharField(max_length=2000, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(blank=True, default=timezone.now, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='active', verbose_name='Статус')

    def __str__(self):
        return "{} - {}".format(self.name, self.email)

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'
