from django import forms
from django.forms import ModelForm
from .models import Faction


class FactionCreationForm(ModelForm):

    class Meta:
        model = Faction
        fields = ('name', 'description', 'emblem')
