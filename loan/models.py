from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer
from datetime import date
from employeedetail.models import EmployeeDetail


# Create your models here.
class Loan(models.Model):
    # account Details
    entityAccountNo = models.CharField(max_length=15, null=True, blank=True)
    submittedBy = models.ForeignKey(User, related_name="appliedby", on_delete=models.CASCADE, null=True, blank=True) # amisis name
    expectedDisbursementDate = models.DateField(null=True, blank=True)
    
    # Added may 26
    lastReturnDate = models.DateField(null=True, blank=True)
    willSaving = models.FloatField(default=0, null=True, blank=True)
    
    # approvedPrincipal
    loanId = models.IntegerField(null=True, blank=True)
    submittedOnDate = models.DateField(default=date.today) # timeline.submittedOnDate
    totalSaving = models.FloatField()
    totalShares = models.FloatField()
    # activeLoanPlanExist = models.BooleanField(default=False)

    customer = models.ForeignKey(Customer, related_name="loans", on_delete=models.CASCADE)
    prcntServiceCharge = models.FloatField(default=8)
    prcntLifeInsurance = models.FloatField(default=3)
    multiplier = models.FloatField(default=4.0) # derived

    flatServiceCharge = models.FloatField(default=0) # sch
    flatLifeInsurance = models.FloatField(default=0) # lis
    tembr = models.FloatField(default=5) #
    
    serviceChargeExtra = models.FloatField(default=0)
    approvedPrincipal = models.FloatField(default=0)
    approvedPrincipalDisbursed = models.FloatField(default=0)
    schFromLoan = models.BooleanField(default=False)
    byDelegation = models.BooleanField(default=False)

    annualInterestRate = models.FloatField(default=0) # ብደሩን የሚወስዱበት የወለድ መጠን (%)
    numberOfRepayments = models.IntegerField(default=0, null=True, blank=True) # ብድሩ የሚመለስበት አመት The year in which the loan will be repaid amisisLoans.numberOfRepayments = months
    totalDueForPeriod = models.FloatField(default=0, null=True, blank=True) # ወርሃዊ ክፍያ Monthly Payment
    totalInterestPayment = models.FloatField(default=0, null=True, blank=True) # ጠቅላላ የወለድ ክፍያ Total interest payment
    queueTime = models.IntegerField(default=5, null=True, blank=True) # የወረፋ ጊዜ
    queueDate = models.DateField(default=date.today, null=True, blank=True) # የወረፋ ቀን 
    

    loanProductId = models.IntegerField(default=0, null=True, blank=True)
    loanProductName= models.CharField(max_length=255, null=True, blank=True)
    loanPurposeId = models.IntegerField(default=0, null=True, blank=True)
    loanPurposeName= models.CharField(max_length=255, null=True, blank=True)

    # To Distributor
    todistributor = models.BooleanField(default=False)
    distributorid = models.ForeignKey(User, related_name="distributor", on_delete=models.SET_NULL, blank=True, null=True) 
    distributorcomment = models.TextField(null=True, blank=True)
    assignedTo = models.ForeignKey(User, related_name="assignedTo", on_delete=models.SET_NULL, blank=True, null=True)

    # Officer
    officerchecking = models.BooleanField(default=False)
    officerid = models.ForeignKey(User, related_name="Officer", on_delete=models.SET_NULL, blank=True, null=True)
    officerapproved = models.BooleanField(default=False)
    officerat = models.DateField(auto_now=True)

    # Team Leader
    teamleaderchecking = models.BooleanField(default=False)
    teamleaderid = models.ForeignKey(User, related_name="teamleader", on_delete=models.SET_NULL, blank=True, null=True) 
    teamleaderapproved = models.BooleanField(default=False)
    teamleaderat = models.DateField(auto_now=True)
    
    # To Auditor / Decision Maker
    auditorchecking = models.BooleanField(default=False)
    auditorid = models.ForeignKey(User, related_name="auditor", on_delete=models.SET_NULL, blank=True, null=True) 
    auditorapproved = models.BooleanField(default=False)
    auditorat = models.DateField(auto_now=True)

    # Dibursement Information
    isDisbursed = models.BooleanField(default=False)

    class Meta:
        unique_together = ("loanId", "customer", "submittedOnDate" )

    def __str__(self):
        return self.entityAccountNo