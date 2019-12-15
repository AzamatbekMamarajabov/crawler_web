from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    region = models.CharField(max_length=100)



class CarModel(models.Model):
    car_name = models.CharField(max_length=200)
    car_desc = models.TextField()
    car_price = models.DecimalField(max_digits=20, decimal_places=2)
    car_year = models.IntegerField()
    region = models.CharField(max_length=100)
    url = models.CharField(max_length=1000)
    website = models.CharField(max_length=20)

    class Meta:
        db_table = 'cars'
