from django.db import models
from carmodel.models import Car_Model
from carmanufacturer.models import Car_Manufacture
from loan.models import Loan
from django.contrib.auth.models import User
from loanguaranteeperson.models import LoanGuaranteePerson
from checklist.models import CheckList

from subcity.models import Subcity

# Create your models here.
class Collateral_Car(models.Model):
    model = models.ForeignKey(Car_Model, related_name="carmodel", on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, related_name="collateralcar", on_delete=models.CASCADE)
    manufacturedYear = models.ForeignKey(Car_Manufacture, related_name="carmanufacture", on_delete=models.CASCADE)
    cargp = models.ForeignKey(LoanGuaranteePerson, related_name="cargp", on_delete=models.DO_NOTHING , null=True, blank=True)

    chassisNumber = models.CharField(max_length=255)
    engineNumber = models.CharField(max_length=255)

    checkListId = models.ForeignKey(CheckList, related_name="carmanufacturecountry", on_delete=models.CASCADE)
    librebookid = models.CharField(max_length=255)
    
    carPlate = models.CharField(max_length=255)
    insuranceValue = models.FloatField(default=0)
    carCC = models.IntegerField()
    subcity = models.ForeignKey(Subcity, related_name="carsubcity", on_delete=models.CASCADE)
    
    isApproved = models.BooleanField(default=False)
    approvedBy = models.ForeignKey(User, related_name="approvedCar", on_delete=models.CASCADE, null=True, blank=True)
    approvedAt = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.manufacturedYear 
    
