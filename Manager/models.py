from django.db import models


# Create your models here.

class Food_items(models.Model):
    Food_id = models.IntegerField(null=False, unique=True, primary_key=True)
    Food_Name = models.CharField(max_length=225, unique=True)
    Food_Price = models.FloatField()

    def __str__(self):
        return self.Food_Name


class Quantity(models.Model):
    Food_id = models.ForeignKey(Food_items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.Food_id)


class Tables(models.Model):
    Table_id = models.IntegerField(null=False, unique=True, primary_key=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.Table_id


class Available_Towns(models.Model):
    Towns = models.CharField(max_length=225, unique=True)

    def __str__(self):
        return self.Towns
