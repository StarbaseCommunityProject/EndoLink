from django import forms
from django.forms import ModelForm
from .models import ShipEntry


class ShipCreationForm(ModelForm):
    tags = forms.CharField(required=False)
    attributes = forms.CharField(required=False)
    images_upload = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = ShipEntry
        fields = ('ship_name', 'description', 'price', 'price_blueprint')
