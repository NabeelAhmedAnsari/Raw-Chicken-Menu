from django.db import models

# Create your models here.

class ChickenPart(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price_per_kg = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    restaurant_name = models.CharField(max_length=200)
    Name = models.CharField(max_length=200, blank=True)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.restaurant_name} - {self.Name or self.mobile}"