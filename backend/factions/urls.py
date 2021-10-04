from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.factions_overview, name='factions_overview'),
    path('create', views.faction_creation, name='faction_creation')
]
