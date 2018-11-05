from django.db import models
from Manager.models import Food_items
from homedelivery.models import HD_FoodOrder

# Create your models here.
class Customer_Food(models.Model):

    mailId = models.EmailField(max_length=255, null=False)
    Food_Id = models.ForeignKey(Food_items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


class Order_User(models.Model):

    mailId = models.CharField(max_length=255, null=False)
    TokenId = models.ForeignKey(HD_FoodOrder, on_delete=models.CASCADE)
