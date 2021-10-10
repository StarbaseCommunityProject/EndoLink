from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import RefreshToken


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'groups', 'leading_faction', 'member_of_faction']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'id', 'name']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        new_user = User(email=self.validated_data['email'], username=self.validated_data['username'], is_staff=False, is_superuser=False)
        new_user.set_password(self.validated_data['password'])
        new_user.save()

        return new_user


class LogOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefreshToken
        fields = ['refresh']
