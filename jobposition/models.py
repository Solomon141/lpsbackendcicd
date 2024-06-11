from django.db import models

# Create your models here.
class JonbPosition(models.Model):
    enName = models.CharField(max_length=255)
    amName = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.enName 