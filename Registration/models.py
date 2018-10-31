from django.db import models

# Create your models here.
class Admin(models.Model):
    Name = models.CharField(max_length=225)
    email = models.EmailField()