from django.db import models
from datetime import date
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Withdrawal(models.Model):
    # account Details
    id = models.UUIDField(default=uuid.uuid4, unique=True,
          primary_key=True, editable=False)
    externalId = models.CharField(max_length=15, null=True, blank=True)
    # savings
    loanSavingSum = models.FloatField(default=0, null=True, blank=True)
    voluntarySum = models.FloatField(default=0, null=True, blank=True)
    funeralSum = models.FloatField(default=0, null=True, blank=True)
    compulsarySum = models.FloatField(default=0, null=True, blank=True)
    timeDepositSum = models.FloatField(default=0, null=True, blank=True)
    totalSaving = models.FloatField()
    totalShares = models.FloatField()
    
    createdAt = models.DateField(default=date.today)
    plannedby = models.ForeignKey(User, related_name="withdrawplannedby",
                                  on_delete=models.CASCADE, null=True, blank=True)
    
    entityAccountNo = models.CharField(max_length=255)
    displayName = models.CharField(max_length=255)
    amDisplayName = models.CharField(max_length=255)
    entityMobileNo = models.CharField(max_length=15)
    
    # finances
    financeCheking = models.BooleanField(default=False)
    financeid = models.ForeignKey(User, related_name="withdrawfinance", on_delete=models.SET_NULL, blank=True, null=True)
    financeapproved = models.BooleanField(default=False)
    financeat = models.DateField(default=date.today, null=True, blank=True)
    

    def __str__(self):
        return self.externalId