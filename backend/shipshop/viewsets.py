from .serializers import ShipEntrySerializer, ShipImageSerializer, ShipLikeSerializer, ShipWishlistSerializer
from .models import ShipEntry, ShipImage, ShipLike, ShipWishlist
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsCreatorOrReadOnly, IsOwnerOrNoAccess

# API view sets


class ShipEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ship entries to be viewed or edited.
    """
    queryset = ShipEntry.objects.all().order_by('-created_at')
    serializer_class = ShipEntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['price', 'price_blueprint']
    search_fields = ['ship_name', 'creator__username']
    ordering_fields = ['id', 'created_at', 'updated_at']
    ordering = ['id']


class ShipImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ship images to be viewed or edited.
    """
    queryset = ShipImage.objects.all()
    serializer_class = ShipImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = []
    search_fields = []
    ordering_fields = ['id']
    ordering = ['id']


class ShipLikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ship likes to be viewed or edited.
    """
    queryset = ShipLike.objects.all().order_by('-liked_at')
    serializer_class = ShipLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['user__id', 'liked_ship__id']
    search_fields = ['liked_ship__ship_name']
    ordering_fields = ['id', 'liked_at']
    ordering = ['id']


class ShipWishlistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ship wishlists to be viewed or edited.
    """
    queryset = ShipWishlist.objects.all().order_by('-wishlisted_at')
    serializer_class = ShipWishlistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['user__id', 'wishlisted_ship__id']
    search_fields = ['wishlisted_ship__ship_name']
    ordering_fields = ['id', 'wishlisted_at']
    ordering = ['id']
