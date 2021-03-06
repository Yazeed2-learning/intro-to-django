from django.db import models

# Create your models here.
class Product(models.Model): 
    title = models.CharField(max_length=120) # max length is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summery = models.TextField(blank=False, null=False)
    featured = models.BooleanField()