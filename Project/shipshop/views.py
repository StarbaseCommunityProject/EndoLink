from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import ShipEntry, ShipImage
from .forms import ShipCreationForm

# Create your views here.


def catalogue(request):
    ships = ShipEntry.objects.all()
    return HttpResponse(render(request, 'shipshop/catalogue.html', {'ships': ships}))


@login_required
def ship_creation(request):
    form = ShipCreationForm(request.POST)
    if form.is_valid() and request.POST:
        ship = form.save(commit=False)
        ship.creator = request.user
        ship.save()

        for image in request.FILES.getlist("images_upload"):
            new_ship_image = ShipImage(image=image)
            new_ship_image.save()
            ship.images.add(new_ship_image)

    return HttpResponse(render(request, 'shipshop/ship_creation.html', {'form': form}))
