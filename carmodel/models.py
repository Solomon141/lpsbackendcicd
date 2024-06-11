from django.db import models

# Create your models here.
class Car_Model(models.Model):
    enName = models.CharField(max_length=255)

    class Meta:
        unique_together = ("id", "enName" )
     
    def __str__(self):
        return self.enName 