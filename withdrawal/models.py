from django.db import models
from datetime import date
from loan.models import Loan
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Disbursement(models.Model):
    # account Details
    externalId = models.CharField(max_length=15, null=True, blank=True)
    loan = models.ForeignKey(Loan, related_name="withdrawloan", on_delete=models.CASCADE)
    
    # savings
    willSaving = models.FloatField(default=0, null=True, blank=True)
    totalSaving = models.FloatField()
    totalShares = models.FloatField()

    # Dibursement Information
    isDisbursed = models.BooleanField(default=False)

    def __str__(self):
        return self.externalId