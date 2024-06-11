from django.db import models
from subcity.models import Subcity

# Create your models here.
class Woreda(models.Model):
    parent = models.ForeignKey(Subcity, related_name="woredas", on_delete=models.CASCADE)
    enName = models.CharField(max_length=255)
    amName = models.CharField(max_length=255)
    isActive = models.BooleanField(default = True)

    class Meta:
        unique_together = ( "parent", "enName", "amName" )


    def __str__(self):
        return self.amName 