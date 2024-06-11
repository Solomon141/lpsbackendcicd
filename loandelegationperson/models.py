from django.db import models
from loan.models import Loan

# Create your models here.
class LoanDelegationPerson(models.Model):
    loan = models.ForeignKey(Loan, related_name="loandelegationperson", on_delete=models.CASCADE)
    isMarried = models.BooleanField()
    fullname = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname