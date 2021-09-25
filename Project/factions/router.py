from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()
router.register(r'factions', viewsets.FactionViewSet)
router.register(r'faction_members', viewsets.FactionMemberViewSet)
router.register(r'faction_roles', viewsets.FactionRoleViewSet)
router.register(r'faction_invitations', viewsets.FactionInvitationViewSet)
router.register(r'faction_advertisements', viewsets.FactionAdvertisementViewSet)
