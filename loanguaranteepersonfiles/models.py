from django.db import models
from loanguaranteeperson.models import LoanGuaranteePerson
from django.contrib.auth.models import User

# Create your models here.
class LoanGuaranteePersonFiles(models.Model):
    guaranteeperson = models.ForeignKey(LoanGuaranteePerson, related_name="loanguaranteeperson", on_delete=models.CASCADE)
    fileType = models.CharField(max_length=25, null=True, blank=True)
    fileUrl = models.FileField(upload_to='lps_django_2024/uploads/', null=True, blank=True)
    user = models.ForeignKey(User, related_name="guaranteepersonuploaduser", on_delete=models.CASCADE, null=True, blank=True)
    uploadedAt = models.DateField(auto_now_add=True)
    amDesc = models.CharField(max_length=255, null=True, blank=True)
   
    def __str__(self):
        return self.amDesc