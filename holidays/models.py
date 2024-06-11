from django.db import models

# Create your models here.
class Holiday(models.Model):
    holidayName = models.CharField(max_length=255)
    holyDate = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.holidayName