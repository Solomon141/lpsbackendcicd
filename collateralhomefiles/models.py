from django.db import models
from django.contrib.auth.models import User
from checklist.models import CheckList
from collateralhome.models import CollateralHome
# Create your models here.

class CollateralHomeFiles(models.Model):
    parent = models.ForeignKey(CollateralHome, related_name="homefiles", on_delete=models.CASCADE)
    fileType = models.CharField(max_length=25, null=True, blank=True)
    fileUrl = models.FileField(upload_to='lps_django_2024/uploads/', null=True, blank=True)
    user = models.ForeignKey(User, related_name="homeuploaduser", on_delete=models.CASCADE, null=True, blank=True)
    uploadedAt = models.DateField(auto_now_add=True)
    amDesc = models.CharField(max_length=255, null=True, blank=True)
    checkListId = models.ForeignKey(CheckList, related_name="homefileschecklist", on_delete=models.CASCADE)
    isUploaded = models.BooleanField(default=False)
    isMandatory = models.BooleanField(default=True)
   
    class Meta:
        unique_together = ("parent", "checkListId" )

    def __str__(self):
        return self.amDesc