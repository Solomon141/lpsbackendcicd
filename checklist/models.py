from django.db import models
from checklisttype.models import CheckListType

# Create your models here.
class CheckList(models.Model):
    parent = models.ForeignKey(CheckListType, related_name="checklists", on_delete=models.CASCADE)
    enName = models.CharField(max_length=255, null=True, blank=True)
    amName = models.CharField(max_length=255)
    isMandatory = models.BooleanField(default = True)
    markValue = models.IntegerField(default=5)

    class Meta:
        unique_together = ( "parent", "enName", "amName" )


    def __str__(self):
        return self.enName 