from django.urls import path
from User import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index),
]+static(settings.STATICS_URL, document_root=settings.STATIC_ROOT)
