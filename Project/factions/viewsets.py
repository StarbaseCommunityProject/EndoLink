from .serializers import FactionSerializer, FactionMemberSerializer, FactionRoleSerializer, FactionInvitationSerializer, FactionAdvertisementSerializer
from .models import Faction, FactionMember, FactionRole, FactionInvitation, FactionAdvertisement
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsLeaderOrReadOnly, InvitePermission

# API view sets


class FactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows factions to be viewed or edited.
    """
    queryset = Faction.objects.all().order_by('-created_at')
    serializer_class = FactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsLeaderOrReadOnly]


class FactionMemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows faction members to be viewed or edited.
    """
    queryset = FactionMember.objects.all().order_by('-joined_at')
    serializer_class = FactionMemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FactionRoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows faction roles to be viewed or edited.
    """
    queryset = FactionRole.objects.all().order_by('name')
    serializer_class = FactionRoleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FactionInvitationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows faction invitations to be viewed or edited.
    """
    queryset = FactionInvitation.objects.all().order_by('-invited_at')
    serializer_class = FactionInvitationSerializer
    permission_classes = [InvitePermission]


class FactionAdvertisementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows faction advertisements to be viewed or edited.
    """
    queryset = FactionAdvertisement.objects.all()
    serializer_class = FactionAdvertisementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
