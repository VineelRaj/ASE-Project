from django.urls import path
from Homepage import views

urlpatterns = [
    path("",views.default )
]
