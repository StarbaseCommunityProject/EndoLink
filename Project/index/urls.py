from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_player_count', views.GetPlayerCountView.as_view(), name='get_player_count'),
    path('get_starbase_news', views.GetStarbaseNewsView.as_view(), name='get_starbase_news'),
]