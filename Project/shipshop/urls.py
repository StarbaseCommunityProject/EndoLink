from django.urls import path

from . import views

urlpatterns = [
    path('catalogue', views.catalogue, name='catalogue'),
    path('ship_creation', views.ship_creation, name='ship_creation'),
]