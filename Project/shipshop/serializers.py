from .models import ShipEntry, ShipImage, ShipLike, ShipWishlist
from rest_framework import serializers


class ShipEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShipEntry
        fields = ['url', 'id', 'creator', 'ship_name', 'description', 'tags', 'attributes', 'images', 'price', 'price_blueprint', 'created_at', 'updated_at', 'is_public', 'like_users', 'wishlist_users']


class ShipImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShipImage
        fields = ['url', 'id', 'image', 'description']


class ShipLikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShipLike
        fields = ['url', 'id', 'user', 'liked_ship', 'liked_at']


class ShipWishlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShipWishlist
        fields = ['url', 'id', 'user', 'wishlisted_ship', 'wishlisted_at']
