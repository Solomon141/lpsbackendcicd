from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class EmployeeDetail(models.Model):
    # parent = models.ForeignKey(User, related_name="employees", on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
   
    firstname = models.CharField(max_length=255, null=True, blank=True)
    amFirstname = models.CharField(max_length=255, null=True, blank=True)
    middlename = models.CharField(max_length=255, null=True, blank=True)
    amMiddlename = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    amLastname = models.CharField(max_length=255, null=True, blank=True)
  
    gender = models.CharField(max_length=15, null=True, blank=True)  # gender.name
    mobileNo = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    amAddress = models.CharField(max_length=255, null=True, blank=True)

    loanExternalID = models.IntegerField(null=True, blank=True)

    dateOfBirth = models.DateField(default=date.today)
    isMarried = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.amFirstname
