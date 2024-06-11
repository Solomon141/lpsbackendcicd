from django.db import models

# Create your models here.
class Car_Manufacture(models.Model):
    yearRange = models.CharField(max_length=255)
    multiplierRatio = models.FloatField()
     
    def __str__(self):
        return self.yearRange 