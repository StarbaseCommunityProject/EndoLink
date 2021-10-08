from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'groups', 'leading_faction', 'member_of_faction']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'id', 'name']


class RegisterSerializer(serializers.ModelSerializer):

    password_repeat = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_repeat']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        new_user = User(email=self.validated_data['email'], username=self.validated_data['username'], is_staff=False, is_superuser=False)
        password = self.validated_data['password']

        if password != self.validated_data['password_repeat']:
            raise serializers.ValidationError({'error': "Passwords don't match."})

        new_user.set_password(password)
        new_user.save()

        return new_user


