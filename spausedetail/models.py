from django.db import models
from datetime import date
from customer.models import Customer
from subcity.models import Subcity

class SpauseDetail(models.Model):
    parent = models.ForeignKey(Customer, related_name="spausedetail", on_delete=models.CASCADE)
    amFullName = models.CharField(max_length=255)
    gender = models.CharField(max_length=15)  # gender.name
    mobileNo = models.CharField(max_length=15)
    amSubcity = models.ForeignKey(Subcity, related_name="spausesubcity", on_delete=models.CASCADE)
    woreda = models.CharField(max_length=255, null=True, blank=True)
    amWoreda = models.CharField(max_length=255, null=True, blank=True)
    houseNum = models.CharField(max_length=255, null=True, blank=True)
    idNum = models.CharField(max_length=255, null=True, blank=True)
    monthlyIncome = models.FloatField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = ( "mobileNo", "amFullName" )

    def __str__(self):
        return self.amFullName
