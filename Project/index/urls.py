from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_player_count', views.get_player_count, name='get_player_count'),
]