from django.urls import path, include

from . import views

urlpatterns = [
    path('factions', views.factions_overview, name='factions_overview')
]
