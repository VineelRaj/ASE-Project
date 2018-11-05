from django.contrib import admin
from .models import Food_items, Quantity, Tables, Available_Towns

# Register your models here.
admin.site.register((Food_items, Quantity, Tables, Available_Towns))
