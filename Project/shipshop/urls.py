from django.urls import path

from . import views

urlpatterns = [
    path('catalogue', views.catalogue, name='catalogue'),
    path('ship_creation', views.ship_creation, name='ship_creation'),
    path('ship_search', views.ship_search, name='ship_search'),
    path('like_ship/<int:ship_id>', views.like_ship, name='like_ship'),
    path('unlike_ship/<int:ship_id>', views.unlike_ship, name='unlike_ship'),
    path('wishlist_ship/<int:ship_id>', views.wishlist_ship, name='wishlist_ship'),
    path('unwishlist_ship/<int:ship_id>', views.unwishlist_ship, name='unwishlist_ship'),
]