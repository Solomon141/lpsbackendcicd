from django.db import models
from datetime import date
from loan.models import Loan
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Disbursement(models.Model):
    # account Details
    externalId = models.CharField(max_length=15, null=True, blank=True)
    loan = models.ForeignKey(Loan, related_name="disbursement_detail", on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    
    # plan Details
    plannedby = models.ForeignKey(User, related_name="plannedby", on_delete=models.CASCADE, null=True, blank=True) # amisis name
    plannedDate = models.DateField(default=date.today, null=True, blank=True)
    
    # Dibursement Information
    appointmentDate = models.DateField(null=True, blank=True)
    
    # approval
    approvedby = models.ForeignKey(User, related_name="approvedby", on_delete=models.CASCADE, null=True, blank=True) # amisis name
    approvedDate = models.DateField(default=date.today, null=True, blank=True)
    
    # disbursement
    disbursedby = models.ForeignKey(User, related_name="disbursedby", on_delete=models.CASCADE, null=True, blank=True) 
    disbursedDate = models.DateField(null=True, blank=True)
    
    # Check
    checkId = models.CharField(max_length=255, null=True, blank=True)
    checksignedby = models.ForeignKey(User, related_name="checksignedby", on_delete=models.CASCADE, null=True, blank=True)
    checkSignedDate = models.DateField(null=True, blank=True)
    isDisbursed = models.BooleanField(default=False)

    def __str__(self):
        return self.externalId