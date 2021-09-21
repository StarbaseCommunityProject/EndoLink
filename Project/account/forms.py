from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import UserExtraInfo


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AccountEditForm(ModelForm):

    class Meta:
        model = UserExtraInfo
        fields = ('in_game_name', 'discord_name', 'forum_name', 'bio', 'home_origin', 'profile_picture')
