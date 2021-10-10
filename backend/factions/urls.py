from django.urls import path

from . import views

urlpatterns = [
    path('create_faction', views.FactionCreationView.as_view(), name='create_faction')
]
