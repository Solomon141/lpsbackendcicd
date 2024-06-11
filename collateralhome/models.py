from django.db import models
from hometype.models import HomeType
from loan.models import Loan
from loanguaranteeperson.models import LoanGuaranteePerson

from subcity.models import Subcity
from django.contrib.auth.models import User

# Create your models here.
class CollateralHome(models.Model):
    hometype = models.ForeignKey(HomeType, related_name="hometype", on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, related_name="collateralhome", on_delete=models.CASCADE)
    homegp = models.ForeignKey(LoanGuaranteePerson, related_name="homegp", on_delete=models.DO_NOTHING , null=True, blank=True)

    locationtxt = models.CharField(max_length=255)
    bldgno = models.CharField(max_length=255, null=True, blank=True)
    floorno = models.CharField(max_length=255, null=True, blank=True)
    subcity = models.ForeignKey(Subcity, related_name="homesubcity", on_delete=models.CASCADE)
    woreda = models.CharField(max_length=255)
    houseno = models.CharField(max_length=255)

    uniquenum = models.CharField(max_length=255)
    amName = models.CharField(max_length=255)
    homearea = models.FloatField()
    
    createdBy = models.ForeignKey(User, related_name="collateralhomeinsertedby", on_delete=models.CASCADE, null=True, blank=True)
    createdAt = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.uniquenum 