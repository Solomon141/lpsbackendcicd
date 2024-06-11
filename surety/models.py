from django.db import models
from datetime import date
from loan.models import Loan

# Create your models here.
class Surety(models.Model):
    loan = models.ForeignKey(Loan, related_name="loansurety", on_delete=models.CASCADE)
    fullName = models.CharField(max_length=255)
    amFullName = models.CharField(max_length=255)
    gender = models.CharField(max_length=15)  # gender.name

    mobileNo = models.CharField(max_length=15)
    subcity = models.CharField(max_length=255, null=True, blank=True)
    amSubcity = models.CharField(max_length=255, null=True, blank=True)
    woreda = models.CharField(max_length=255, null=True, blank=True)
    houseNum = models.CharField(max_length=255, null=True, blank=True)
    idnum = models.CharField(max_length=255, null=True, blank=True)
    createdAt = models.DateField(default=date.today)

    def __str__(self):
        return self.amFullName