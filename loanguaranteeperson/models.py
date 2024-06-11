from django.db import models
from loan.models import Loan


# Create your models here.
class LoanGuaranteePerson(models.Model):
    loan = models.ForeignKey(Loan, related_name="gp", on_delete=models.CASCADE)
    isMarried = models.BooleanField()
    fullname = models.CharField(max_length=255, null=True)

    subcity = models.CharField(max_length=255, null=True)
    woreda = models.CharField(max_length=255, null=True)
    housenum = models.CharField(max_length=255, null=True)
    idnum = models.CharField(max_length=255, null=True)
    phonenum = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.fullname