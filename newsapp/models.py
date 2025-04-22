# newspapp/models.py
from django.db import models

class UserInterest(models.Model):
    interest = models.CharField(max_length=100)

    def __str__(self):
        return self.interest

# Create your models here.
