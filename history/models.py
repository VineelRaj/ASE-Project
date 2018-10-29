from django.db import models

class foodorders(models.Model):
   foodname=models.CharField(max_length=256)
   date=models.DateField()
   price=models.DecimalField(max_digits=10,decimal_places=2)
   username=models.CharField(max_length=256)
   quantity=models.IntegerField()

class date(models.Model):
      FROM=models.DateField(auto_now=False,auto_now_add=False)
      TO=models.DateField(auto_now=False,auto_now_add=False)


class new1(models.Model):
    item=models.CharField(max_length=200)
    frequency=models.IntegerField()
from django.db import models

# Create your models here.
