from django.urls import path, include

from . import views


# TODO: Potentially remove "account" base url, and move that to the main urlpatterns instead?

urlpatterns = [
    path('', include('django.contrib.auth.urls')),  # Default Django auth module.
    path('signup', views.signup, name='signup'),
    path('', views.account_page, name='account'),
    # path('account/edit', views.account_edit_page, name='edit')
]
