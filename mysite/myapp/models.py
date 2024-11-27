from django.db import models

# Create your models here.
class Invoice(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=14)
    address=models.CharField(max_length=200)
    product=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    summary=models.CharField(max_length=200)

