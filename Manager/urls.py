from django.urls import path
from Manager import views


urlpatterns = [
    path('', views.index, name='index'),
    path('food_home/', views.food_home, name='food_home'),
    path('tables_home/', views.tables_home, name='tables_home'),
    path('add_food/', views.add_food, name='add_food'),
    path('remove_food/', views.remove_food, name='remove_food'),
    path('add_tables/', views.add_tables, name='add_tables'),
    path('remove_tables/', views.remove_tables, name='remove_tables'),
    path('update_food/', views.update_food, name='update_food'),
    path('check_update_food/', views.check_update_food , name='check_update_food'),
    path('town_home/', views.town_home, name='town_home'),
    path('add_towns/', views.add_towns, name='add_towns'),
    path('remove_towns/', views.remove_towns, name='remove_towns'),
    path('update_table/', views.update_table, name='update_table'),
    path('check_update_table/', views.check_update_table , name='check_update_table'),
]
