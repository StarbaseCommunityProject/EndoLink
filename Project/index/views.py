from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import os

# Create your views here.


def index(request):
    return HttpResponse(render(request, 'index/index.html'))


def get_player_count(request):
    api_key = os.getenv('STEAM_API_KEY', '')
    app_id = 454120

    starbase_player_count_url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?key={api_key}&format=json&appid={app_id}"
    player_count_request = requests.get(starbase_player_count_url)
    return JsonResponse({'player_count': player_count_request.json()['response']['player_count']})
