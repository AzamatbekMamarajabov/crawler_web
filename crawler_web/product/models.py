from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    region = models.CharField(max_length=100)