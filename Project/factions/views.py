from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import FactionCreationForm
from .models import Faction, FactionMember

# Create your views here.


def factions_overview(request):
    return HttpResponse(render(request, 'factions/overview.html'))


@login_required
def faction_creation(request):
    form = FactionCreationForm(request.POST)
    if form.is_valid() and request.POST:
        if Faction.objects.filter(leader=request.user).count() == 0 and FactionMember.objects.filter(user=request.user).count() == 0:
            new_faction = form.save(commit=False)
            new_faction.leader = request.user
            new_faction.save()
            new_faction_member = FactionMember(user=request.user, faction=new_faction)
            new_faction_member.save()

    return HttpResponse(render(request, 'factions/faction_creation.html', {'form': form}))

