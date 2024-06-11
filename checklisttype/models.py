from django.db import models

# Create your models here.
class CheckListType(models.Model):
    enName = models.CharField(max_length=255)
    amName = models.CharField(max_length=255)

    class Meta:
        unique_together = ("enName", "amName" )

    def __str__(self):
        return self.enName 