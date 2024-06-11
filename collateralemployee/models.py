from django.db import models
from loan.models import Loan
from checklist.models import CheckList
from django.contrib.auth.models import User
from subcity.models import Subcity

# Create your models here.
class Collateral_Employee(models.Model):
    loan = models.ForeignKey(Loan, related_name="collateralemployee", on_delete=models.CASCADE)
    empName = models.CharField(max_length=255)
    empAmName = models.CharField(max_length=255)
    grossSalary = models.FloatField(null=True, blank=True)
    companyname = models.CharField(max_length=255, null=True, blank=True)
    checkListId = models.ForeignKey(CheckList, related_name="companytype",  on_delete=models.CASCADE )
    companyage = models.IntegerField()
    mobileNo = models.CharField(max_length=15, null=True, blank=True)
    empPhoneNum = models.CharField(max_length=15, null=True, blank=True)

    idNum = models.CharField(max_length=25, null=True, blank=True)
    letterNum = models.CharField(max_length=25, null=True, blank=True)
    subcity = models.ForeignKey(Subcity, related_name="cempsubcity", on_delete=models.CASCADE)
    woreda = models.CharField(max_length=25, null=True, blank=True)
    
    createdBy = models.ForeignKey(User, related_name="collateralempsinsertedby", on_delete=models.CASCADE, null=True, blank=True)
    createdAt = models.DateField(auto_now_add=False, null=True, blank=True)
    isApproved = models.BooleanField(default=False)
    approvedBy = models.ForeignKey(User, related_name="approvedEmployee", on_delete=models.CASCADE, null=True, blank=True)
    approvedAt = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.empName 