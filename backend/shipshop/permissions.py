from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow creators of a ship to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Superusers are allowed to edit anything.
        if request.user.is_superuser:
            return True

        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the ship entry.
        return obj.creator == request.user


class IsOwnerOrNoAccess(permissions.BasePermission):
    """
    Custom permission to only allow the user who liked / wishlisted a ship to read & interact with said like / wishlist.
    """

    def has_object_permission(self, request, view, obj):
        # Superusers are allowed to edit anything.
        if request.user.is_superuser:
            return True

        # Permissions are only allowed to the creator of the like / wishlist entry.
        return obj.user == request.user
