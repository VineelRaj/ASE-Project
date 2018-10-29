from django.urls import path
from Manager import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_food, name='add'),
    path('remove/', views.remove_food, name='remove'),
]
