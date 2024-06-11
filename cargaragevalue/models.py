from django.db import models
from django.contrib.auth.models import User
from collateralcar.models import Collateral_Car

# Create your models here.
class GarageReport(models.Model):
    collateralcar = models.ForeignKey(Collateral_Car, related_name="garageReport", on_delete=models.CASCADE)
    fileType = models.CharField(max_length=25, null=True, blank=True)
    fileUrl = models.FileField(upload_to='lps_django_2024/uploads/', null=True, blank=True)
    user = models.ForeignKey(User, related_name="garageuser", on_delete=models.CASCADE, null=True, blank=True)
    uploadedAt = models.DateField(auto_now_add=True)
    amDesc = models.CharField(max_length=255, default="የጋራጅ ሪፖርት", null=True, blank=True)
    garageValue = models.FloatField(default=0)
    isUploaded = models.BooleanField(default=False)

    isApproved = models.BooleanField(default=False)
    approvedBy = models.ForeignKey(User, related_name="cgvapprovedBy", on_delete=models.CASCADE, null=True, blank=True)
    approvedAt = models.DateField(auto_now_add=False, null=True, blank=True)
   
    class Meta:
        unique_together = ("id", "collateralcar")

    def __str__(self):
        return self.amDesc 