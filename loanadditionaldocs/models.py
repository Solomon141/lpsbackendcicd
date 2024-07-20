from django.db import models
from django.contrib.auth.models import User
from loan.models import Loan

# Create your models here.
class LoanAdditionalFiles(models.Model):
    additionalfiles = models.ForeignKey(Loan, related_name="loanadditionalfiles", on_delete=models.CASCADE)
    fileType = models.CharField(max_length=25, null=True, blank=True)
    fileUrl = models.FileField(upload_to='lps_django_2024/uploads/', null=True, blank=True)
    user = models.ForeignKey(User, related_name="loanadditionalfilesuser", on_delete=models.CASCADE, null=True, blank=True)
    uploadedAt = models.DateField(auto_now_add=True)
    descript = models.TextField()
    isUploaded = models.BooleanField(default=False)
    isApproved = models.BooleanField(default=False)
    approvedBy = models.ForeignKey(User, related_name="loanadditionalfilesapprove", on_delete=models.CASCADE, null=True, blank=True)
    approvedAt = models.DateField(auto_now_add=False, null=True, blank=True)
   
    def __str__(self):
        return self.descript