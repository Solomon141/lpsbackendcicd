from django.db import models
from datetime import date
from loan.models import Loan
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Disbursement(models.Model):
    # account Details
    externalId = models.CharField(max_length=15, null=True, blank=True)
    loan = models.ForeignKey(
        Loan, related_name="disbursement_detail", on_delete=models.CASCADE)
    amount = models.FloatField(default=0)

    # plan Details
    plannedby = models.ForeignKey(User, related_name="plannedby",
                                  on_delete=models.CASCADE, null=True, blank=True)  # amisis name
    plannedDate = models.DateField(default=date.today, null=True, blank=True)

    # Dibursement Information
    appointmentDate = models.DateField(null=True, blank=True)
    disbursedby = models.ForeignKey(
        User, related_name="disbursedby", on_delete=models.CASCADE, null=True, blank=True)
    disbursedDate = models.DateField(null=True, blank=True)

    # Check from finances
    checkId = models.CharField(max_length=255, null=True, blank=True)
    checkissuedby = models.ForeignKey(
        User, related_name="checkissuedby", on_delete=models.CASCADE, null=True, blank=True)
    checksignedby = models.TextField( null=True, blank=True)
    checkIssuedDate = models.DateField(null=True, blank=True)
    isDisbursed = models.BooleanField(default=False)

    def str(self):
        return self.externalId