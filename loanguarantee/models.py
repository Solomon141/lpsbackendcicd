from django.db import models
from loan.models import Loan
from django.contrib.auth.models import User
from checklist.models import CheckList
# Create your models here.

class LoanGuaranteeFiles(models.Model):
    loan = models.ForeignKey(Loan, related_name="loanguarantee", on_delete=models.CASCADE)
    fileType = models.CharField(max_length=25, null=True, blank=True)
    fileUrl = models.FileField(upload_to='lps_django_2024/uploads/', null=True, blank=True)
    user = models.ForeignKey(User, related_name="guaranteeuploaduser", on_delete=models.CASCADE, null=True, blank=True)
    uploadedAt = models.DateField(auto_now_add=True)
    amDesc = models.CharField(max_length=255, null=True, blank=True)
    checkListId = models.ForeignKey(CheckList, related_name="guaranteechecklist", on_delete=models.CASCADE)
    isUploaded = models.BooleanField(default=False)

    isApproved = models.BooleanField(default=False)
    approvedBy = models.ForeignKey(User, related_name="approvedLoanGuarantee", on_delete=models.CASCADE, null=True, blank=True)
    approvedAt = models.DateField(auto_now_add=False, null=True, blank=True)
   
    class Meta:
        unique_together = ("loan", "checkListId" )

    def __str__(self):
        return self.amDesc