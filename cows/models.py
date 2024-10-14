from django.db import models


class Cow(models.Model):
    name = models.CharField(max_length=50, null=False)
    color = models.CharField(max_length=50, null=False)
    breed = models.CharField(max_length=50, null=True)
    features = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
