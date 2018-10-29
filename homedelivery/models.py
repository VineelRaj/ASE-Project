from django.db import models
from Manager.models import Food_items
from django.core.validators import MinValueValidator, RegexValidator


# Create your models here.


class HD_FoodOrder(models.Model):
    tokenId = models.AutoField(primary_key=True)
    quantity = models.PositiveIntegerField(null=False)
    price = models.FloatField(validators=[MinValueValidator(0.0)], null=False)
    Food_id = models.ForeignKey(Food_items, on_delete=models.CASCADE)
    date = models.DateTimeField()


class HD_Address(models.Model):
    tokenId = models.ForeignKey(HD_FoodOrder, on_delete=models.CASCADE)
    town = models.CharField(max_length=225, null=False)
    street = models.CharField(max_length=225, null=False)
    dNo = models.PositiveIntegerField(null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
