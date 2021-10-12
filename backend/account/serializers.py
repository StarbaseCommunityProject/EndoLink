from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import UserExtraInfo


class NestedUserExtraInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserExtraInfo
        fields = ['in_game_name', 'discord_name', 'forum_name', 'bio', 'home_origin', 'profile_picture']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile_picture = serializers.ImageField(source='userextrainfo.profile_picture', read_only=True)
    extra_info = NestedUserExtraInfoSerializer(source='userextrainfo', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password', 'email', 'groups', 'leading_faction', 'member_of_faction', 'profile_picture', 'extra_info']
        extra_kwargs = {'leading_faction': {'read_only': True}, 'password': {'write_only': True, 'required': True}}

    def save(self, **kwargs):
        user = super(UserSerializer, self).save(**kwargs)
        user.set_password(self.validated_data['password'])
        user.save()

        return user

    def create(self, validated_data):
        new_user = super(UserSerializer, self).create(validated_data)

        new_user_extra_info = UserExtraInfo(user=new_user)
        new_user_extra_info.save()

        return new_user

    def update(self, instance, validated_data):
        user = super(UserSerializer, self).update(instance, validated_data)
        if self.validated_data.get('password', None):
            user.set_password(self.validated_data['password'])
            user.save()
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'id', 'name']


class RegisterSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def validate(self, data):
        try:
            validate_password(password=data.get('password'), user=User(username=data.get('username'), email=data.get('email')))
        except ValidationError as e:
            raise ValidationError({'password': list(e.messages)})

        return super(RegisterSerializer, self).validate(data)

    def save(self, **kwargs):
        new_user = User(email=self.validated_data['email'], username=self.validated_data['username'], is_staff=False, is_superuser=False)
        new_user.set_password(self.validated_data['password'])
        new_user.save()

        new_user_extra_info = UserExtraInfo(user=new_user, profile_picture=self.validated_data.get('profile_picture', None))
        new_user_extra_info.save()

        return new_user


class LogOutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(write_only=True)


class LogOutAllSerializer(serializers.Serializer):
    pass
