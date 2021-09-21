from django.urls import path, include

from . import views


# TODO: Potentially remove "account" base url, and move that to the main urlpatterns instead?

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),  # Default Django auth module.
    path('account/signup', views.signup, name='signup'),
    path('account', views.account_page, name='account'),
    # path('account/edit', views.account_edit_page, name='edit')
]
