from django.db import models

# Create your models here.

class Campsites(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()
    amenities = models.CharField(max_length=255, help_text="Comma-separated list")
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    
    

    def __str__(self):
        return self.name