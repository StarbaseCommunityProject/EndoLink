from django.shortcuts import render
from django.http import HttpResponse
from .models import ShipEntry

# Create your views here.


def catalogue(request):
    ships = ShipEntry.objects.all()
    return HttpResponse(render(request, 'shipshop/catalogue.html', {'ships': ships}))
