from django.db import models
from collateralstock.models import CollateralStock
from django.contrib.auth.models import User
from checklist.models import CheckList

# Create your models here.
class CollateralStockFiles(models.Model):
    parent = models.ForeignKey(CollateralStock, related_name="stockfiles", on_delete=models.CASCADE)
    fileType = models.CharField(max_length=25, null=True, blank=True)
    fileUrl = models.FileField(upload_to='lps_django_2024/uploads/', null=True, blank=True)
    user = models.ForeignKey(User, related_name="collateralstockuser", on_delete=models.CASCADE, null=True, blank=True)
    uploadedAt = models.DateField(auto_now_add=True)
    amDesc = models.CharField(max_length=255, null=True, blank=True)
    checkListId = models.ForeignKey(CheckList, related_name="stockfileschecklist", on_delete=models.CASCADE)
    isUploaded = models.BooleanField(default=False)
    isMandatory = models.BooleanField(default=True)
   
    def __str__(self):
        return self.amDesc