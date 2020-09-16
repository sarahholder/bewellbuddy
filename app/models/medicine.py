from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    comments = models.CharField(max_length=250)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    uploadImg = models.CharField(max_length=500)




