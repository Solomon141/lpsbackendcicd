from django.db import models
from datetime import date

# Create your models here.
class WithdrawCustomer(models.Model):
    entityAccountNo = models.CharField(max_length=255)
    entityExternalId = models.IntegerField()
    activationDate = models.DateField()
    active=models.BooleanField()
    memberSince = models.DateField(default=date.today)

    displayName = models.CharField(max_length=255)
    amDisplayName = models.CharField(max_length=255)

    firstname = models.CharField(max_length=255)
    amFirstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255)
    amMiddlename = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    amLastname = models.CharField(max_length=255)
  
    gender = models.CharField(max_length=15)  # gender.name
    mobileNo = models.CharField(max_length=15)
    address = models.CharField(max_length=255, null=True, blank=True)
    amAddress = models.CharField(max_length=255, null=True, blank=True)

    subcity = models.CharField(max_length=255, null=True, blank=True)
    amSubcity = models.CharField(max_length=255, null=True, blank=True)
    woreda = models.CharField(max_length=255, null=True, blank=True)
    houseNum = models.CharField(max_length=255, null=True, blank=True)
    idNum = models.CharField(max_length=255, null=True, blank=True)
    monthlyIncome = models.FloatField(max_length=255, null=True, blank=True)
    monthlySaving = models.FloatField(max_length=255, null=True, blank=True)
    
    dateOfBirth = models.DateField()
    isMarried = models.BooleanField()

    # Approval 
    isApproved = models.BooleanField(default=False)
    approvedBy = models.BooleanField(default=False)
    approvedAt = models.DateField(null=True, blank=True)
    reviewercomment = models.TextField(blank=True)

    class Meta:
        unique_together = ( "entityAccountNo", "entityExternalId" )

    def __str__(self):
        return self.amDisplayName