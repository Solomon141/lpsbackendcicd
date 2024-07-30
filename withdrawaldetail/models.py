from django.db import models
from datetime import date
from django.contrib.auth.models import User
from withdrawal.models import Withdrawal

# Create your models here.
class WithdrawalDetail(models.Model):
    # account Details
    withdrawaldetail = models.ForeignKey(Withdrawal, related_name="withdrawaldetail", on_delete=models.CASCADE)
    amount = models.FloatField(default=0)

    # plan Details
    plannedby = models.ForeignKey(User, related_name="withdrawalplannedby",
                                  on_delete=models.CASCADE, null=True, blank=True)  # amisis name
    plannedDate = models.DateField(default=date.today, null=True, blank=True)
    appointmentDate = models.DateField(default=date.today, null=True, blank=True)

    # Check from finances
    checkId = models.CharField(max_length=255, null=True, blank=True)
    checksignedby = models.TextField( null=True, blank=True)
    checkissuedby = models.ForeignKey(
        User, related_name="withdrawalcheckissuedby", on_delete=models.CASCADE, null=True, blank=True)
    checkIssuedDate = models.DateField(null=True, blank=True)
    
    # check accepted and processing to give to customers
    isAccepted = models.BooleanField(default=False)
    acceptedBy = models.ForeignKey(
        User, related_name="withdrawalacceptedby", on_delete=models.CASCADE, null=True, blank=True)
    acceptedDate = models.DateField(null=True, blank=True)
    
    isDelivered = models.BooleanField(default=False)
    deliveredBy = models.ForeignKey(
        User, related_name="withdrawalddeliveredby", on_delete=models.CASCADE, null=True, blank=True)
    deliveredDate = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.amount