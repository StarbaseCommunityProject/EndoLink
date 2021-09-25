from rest_framework import permissions


class IsLeaderOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow leaders of a faction to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Superusers are allowed to edit anything.
        if request.user.is_superuser:
            return True

        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the leader of the faction.
        return obj.leader == request.user


class InvitePermission(permissions.BasePermission):
    """
    Custom permission to only allow the user who sent or received the invite, as well as the faction leader, to view the invite
    """

    def has_object_permission(self, request, view, obj):
        # Superusers are allowed to edit anything.
        if request.user.is_superuser:
            return True

        # Read permissions are allowed to the invitee.
        if request.method in permissions.SAFE_METHODS and request.user == obj.user:
            return True

        # Permissions are only allowed to the creator of the invitation or the faction leader.
        return request.user in [obj.invited_by, obj.faction.leader]
