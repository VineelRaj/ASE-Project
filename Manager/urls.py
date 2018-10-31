from django.urls import path
from Manager import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_food/', views.add_food, name='add_food'),
    path('remove_food/', views.remove_food, name='remove_food'),
    path('update_food/', views.update_food, name='update_food'),
    path('check_update_food/', views.check_update_food , name='check_update_food'),
]
