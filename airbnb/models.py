from django.db import models
from accounts.models import UserProfile

class Flat(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(upload_to='flats/', null=True, blank=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name
