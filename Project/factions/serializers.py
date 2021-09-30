from .models import Faction, FactionMember, FactionRole, FactionInvitation, FactionAdvertisement
from rest_framework import serializers


class FactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faction
        fields = ['url', 'id', 'name', 'description', 'tags', 'emblem', 'advertisement', 'leader', 'members', 'invitations', 'roles', 'created_at']


class FactionMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FactionMember
        fields = ['url', 'id', 'user', 'faction', 'roles', 'joined_at']


class FactionRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FactionRole
        fields = ['url', 'id', 'name', 'description']


class FactionInvitationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FactionInvitation
        fields = ['url', 'id', 'user', 'faction', 'invited_by', 'invited_at']


class FactionAdvertisementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FactionAdvertisement
        fields = ['url', 'id', 'image', 'description', 'message']
