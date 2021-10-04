from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()
router.register(r'ships', viewsets.ShipEntryViewSet)
router.register(r'ship_images', viewsets.ShipImageViewSet)
router.register(r'ship_likes', viewsets.ShipLikeViewSet)
router.register(r'ship_wishlists', viewsets.ShipWishlistViewSet)
