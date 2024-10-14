from django.db import models
from lists.models import Staff


class Milking(models.Model):
    datetime = models.DateTimeField(null=False)
    staff_id = models.ForeignKey(Staff, on_delete=models.RESTRICT)
    milk_amount_total = models.FloatField(null=False)
    cows_milked = models.IntegerField(null=False)
    milk_amount_e = models.FloatField()
    milk_amount_v = models.FloatField()
    milk_amount_1 = models.FloatField()
    milk_fat_per = models.FloatField()
    milk_prot_per = models.FloatField()

    def __str__(self):
        return f'{self.datetime} - {self.milk_amount_total} / {self.cows_milked}'
