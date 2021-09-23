from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def factions_overview(request):
    return HttpResponse(render(request, 'factions/overview.html'))
