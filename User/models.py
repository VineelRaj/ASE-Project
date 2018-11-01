from django.db import models

# Create your models here.
class Customer_Food(models.Model):

    mailId = models.CharField(max_length=255, null=False)
    FoodId = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False,default=0)

class Order_User(models.Model):

    mailId = models.CharField(max_length=255, null=False)
    TokenId = models.IntegerField(null=False)
