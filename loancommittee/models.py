from django.db import models
from jobposition.models import JonbPosition

# Create your models here.
class LoanCommittee(models.Model):
    enFullName = models.CharField(max_length=255)
    amFullName = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)
    jobposition = models.ForeignKey(JonbPosition, related_name="jobposition", on_delete=models.CASCADE)

    def __str__(self):
        return self.enFullName 