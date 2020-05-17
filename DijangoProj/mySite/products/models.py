from django.db import models

# Create your models here.

def ProductCategory(models.Model):
    category_name = models.CharField(max_length=200)


def Product(models.Model):
    product_name = models.CharField(max_lengh=200)
    price = models.FloatField()
    is_available = models.BooleanField()
    categories_id = models.ForeignKey(ProductCategory)

