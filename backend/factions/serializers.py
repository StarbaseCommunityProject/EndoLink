from .models import Faction, FactionMember, FactionRole, FactionInvitation, FactionAdvertisement
from rest_framework import serializers


class FactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faction
        fields = ['url', 'id', 'name', 'faction_tag', 'description', 'tags', 'emblem', 'advertisement', 'leader', 'members', 'invitations', 'roles', 'created_at']


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


class FactionCreationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faction
        fields = ['name', 'faction_tag', 'description', 'tags', 'emblem']

    def save(self, **kwargs):
        new_faction = Faction(name=self.validated_data['name'], faction_tag=self.validated_data['faction_tag'], description=self.validated_data['description'], tags=self.validated_data['tags'], emblem=self.validated_data['emblem'], leader=self.validated_data['leader'])
        new_faction.save()

        new_faction_member = FactionMember(user=self.validated_data['leader'], faction=new_faction)
        new_faction_member.save()

        return new_faction
