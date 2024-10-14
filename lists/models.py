from django.db import models
from django.urls import reverse


class Staff(models.Model):
    lastname = models.CharField(max_length=50, null=False)
    firstname = models.CharField(max_length=50, null=False)
    patronymic = models.CharField(max_length=50, null=False)
    post = models.CharField(max_length=50, null=False)
    works = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.lastname} {self.firstname} {self.patronymic}'

    def get_absolute_url(self):
        return reverse('cow_edit', kwargs={'pk': self.pk})
