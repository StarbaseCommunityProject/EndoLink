from django.urls import path, include

from . import views

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),  # Default Django auth module.
    path('account/signup', views.signup, name='signup'),
    path('account', views.account_page, name='account'),
]
