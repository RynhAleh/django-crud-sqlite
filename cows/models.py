from django.db import models
from django.urls import reverse


class Cow(models.Model):
    name = models.CharField(max_length=200, null=False)
    color = models.CharField(max_length=200, null=False)
    breed = models.CharField(max_length=200, null=True)
    features = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cow_edit', kwargs={'pk': self.pk})
