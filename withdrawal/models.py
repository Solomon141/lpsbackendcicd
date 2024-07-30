from django.db import models
from datetime import date
from django.contrib.auth.models import User
from withdrawcustomer.models import WithdrawCustomer
import uuid

# Create your models here.
class Withdrawal(models.Model):
    # account Details
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    customerId = models.ForeignKey(WithdrawCustomer, related_name="tobewithdrawen", on_delete=models.CASCADE )
    # savings
    amount = models.FloatField(default=0)
    savingTypeId = models.IntegerField()
    savingType = models.CharField(max_length=255)
    amSavingType = models.CharField(max_length=255)
    createdAt = models.DateField(default=date.today)
    plannedby = models.ForeignKey(User, related_name="withdrawplannedby",
                                  on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        unique_together = ("customerId", "savingTypeId")

    def __str__(self):
        return self.id