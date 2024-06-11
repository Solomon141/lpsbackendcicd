from django.db import models
from django.contrib.auth.models import User
from checklist.models import CheckList
from customer.models import Customer

# Create your models here.
class CustomerCommonFiles(models.Model):
    parent = models.ForeignKey(Customer, related_name="customercommonfiles", on_delete=models.CASCADE)
    fileType = models.CharField(max_length=25, null=True, blank=True)
    fileUrl = models.FileField(upload_to='lps_django_2024/uploads/', null=True, blank=True)
    user = models.ForeignKey(User, related_name="customercommonfilesinsertedby", on_delete=models.CASCADE, null=True, blank=True)
    uploadedAt = models.DateField(auto_now_add=True)
    amDesc = models.CharField(max_length=255, null=True, blank=True)
    checkListId = models.ForeignKey(CheckList, related_name="custcommonfile", on_delete=models.CASCADE)
    isUploaded = models.BooleanField(default=False)

    isApproved = models.BooleanField(default=False)
    approvedBy = models.ForeignKey(User, related_name="approvedCustomerCommonFile", on_delete=models.CASCADE, null=True, blank=True)
    approvedAt = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.amDesc