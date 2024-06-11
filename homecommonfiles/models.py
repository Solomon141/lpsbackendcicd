from django.db import models
from collateralhome.models import CollateralHome
from django.contrib.auth.models import User
from checklist.models import CheckList
# Create your models here.

class Home_Files(models.Model):
    collateralhome = models.ForeignKey(CollateralHome, related_name="homefiles", on_delete=models.CASCADE)
    fileType = models.CharField(max_length=25, null=True, blank=True)
    fileUrl = models.FileField(upload_to='lps_django_2024/uploads/', null=True, blank=True)
    user = models.ForeignKey(User, related_name="homeuploaduser", on_delete=models.CASCADE, null=True, blank=True)
    uploadedAt = models.DateField(auto_now_add=True)
    amDesc = models.CharField(max_length=255, null=True, blank=True)
    checkListId = models.ForeignKey(CheckList, related_name="homefileschecklist", on_delete=models.CASCADE)
    isUploaded = models.BooleanField(default=False)

    isApproved = models.BooleanField(default=False)
    approvedBy = models.ForeignKey(User, related_name="approvedHomeCommonFiles", on_delete=models.CASCADE, null=True, blank=True)
    approvedAt = models.DateField(auto_now_add=False, null=True, blank=True)
   
    class Meta:
        unique_together = ("collateralhome", "checkListId" )

    def __str__(self):
        return self.amDesc
