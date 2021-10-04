from django.urls import path

from . import views

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
    path('create', views.ship_creation, name='ship_creation'),
    path('search', views.ship_search, name='ship_search'),
    path('like/<int:ship_id>', views.like_ship, name='like_ship'),
    path('unlike/<int:ship_id>', views.unlike_ship, name='unlike_ship'),
    path('wishlist/<int:ship_id>', views.wishlist_ship, name='wishlist_ship'),
    path('unwishlist/<int:ship_id>', views.unwishlist_ship, name='unwishlist_ship'),
    path('wishlist', views.wishlist, name='wishlisted_ships'),
    path('like', views.likes, name='liked_ships'),
]