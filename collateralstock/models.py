from django.db import models
from loan.models import Loan
from loanguaranteeperson.models import LoanGuaranteePerson
from checklist.models import CheckList
from django.contrib.auth.models import User
from subcity.models import Subcity

# Create your models here.
class CollateralStock(models.Model):
    loan = models.ForeignKey(Loan, related_name="collateralstock", on_delete=models.CASCADE)
    stockgp = models.ForeignKey(LoanGuaranteePerson, related_name="stockgp", on_delete=models.DO_NOTHING , null=True, blank=True)
    bankId = models.ForeignKey(CheckList, related_name="stockchecklist", on_delete=models.CASCADE)
    priceperstock = models.FloatField()
    stockqty = models.IntegerField()
    letternum = models.CharField(max_length=255)
    letterdate = models.CharField(max_length=255)
    
    fileType = models.CharField(max_length=25, null=True, blank=True)
    fileUrl = models.FileField(upload_to='lps_django_2024/uploads/', null=True, blank=True)
    uploadedBy = models.ForeignKey(User, related_name="collateralstocksinsertedby", on_delete=models.CASCADE, null=True, blank=True)
    uploadedAt = models.DateField(auto_now_add=False, null=True, blank=True)
    isUploaded = models.BooleanField(default=False)

    isApproved = models.BooleanField(default=False)
    approvedBy = models.ForeignKey(User, related_name="approvedStock", on_delete=models.CASCADE, null=True, blank=True)
    approvedAt = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.letternum 
