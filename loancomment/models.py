from django.db import models
from datetime import date
from loan.models import Loan
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class LoanComment(models.Model):
    loan = models.ForeignKey(Loan, related_name="loancomment", on_delete=models.CASCADE)
    commentedBy = models.ForeignKey(User, related_name="commentedBy", on_delete=models.CASCADE)
    commentedAt = models.DateTimeField(default=timezone.now)
    comment = models.TextField()

    def __str__(self):
        return self.comment