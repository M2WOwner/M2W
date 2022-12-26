from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    Description = models.CharField(max_length=1000)
    Image = models.CharField(max_length=2083)
    # stock = models.IntegerField()

class Offer(models.Model):
    code = models.CharField(max_length=11)
    Description = models.CharField(max_length=255)
    discount = models.FloatField()



