from django.db import models
#from django.contrib.auth.models import User
# Create your models here.

class Admin(models.Model):
    Name = models.CharField(max_length=225,blank=False)
    email = models.EmailField()
    password = models.CharField(max_length = 50,null=True)
    canteen_name = models.CharField(max_length = 200,null=True)
    canteen_street = models.CharField(max_length=200,null=True)
    canteen_pincode = models.IntegerField(null=True)

class User(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=150)
    profile_pic = models.ImageField(upload_to='user_profile_pics',blank=True)

class Staff(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length=200)
    employee_id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=150)
