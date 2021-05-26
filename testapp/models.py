from django.db import models
class Company(models.Model):
    name=models.CharField(max_length=128)
    location=models.CharField(max_length=65)
    ceo=models.CharField(max_length=65)

