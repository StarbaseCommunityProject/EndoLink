from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from drf_yasg.utils import swagger_auto_schema
import requests
import time
import os

# Create your views here.


class GetPlayerCountView(GenericAPIView):
    """
    API endpoint to get the in-game player count.
    """
    # TODO: Potentially log player count to get historical Starbase data?
    filter_backends = []
    pagination_class = None

    cached_player_count = 0
    time_since_player_count_request = time.time() - 5   # Prevents an unlikely call within the first 5 seconds of the site being up from showing 0 users.

    @classmethod
    @swagger_auto_schema(operation_id="get_player_count", tags=["utils"])
    def get(cls, request):
        cached = True
        if time.time() - cls.time_since_player_count_request >= 5:
            cls.time_since_player_count_request = time.time()

            cached = False

            api_key = os.getenv('STEAM_API_KEY', '')
            app_id = 454120

            starbase_player_count_url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?key={api_key}&format=json&appid={app_id}"
            player_count_request = requests.get(starbase_player_count_url)
            cls.cached_player_count = player_count_request.json()['response']['player_count']

        return JsonResponse({'player_count': cls.cached_player_count, 'cached': cached})


class GetStarbaseNewsView(GenericAPIView):
    """
    API endpoint to get the latest Steam news.
    """
    filter_backends = []
    pagination_class = None

    cached_news = ""
    time_since_news_request = time.time() - 1800   # Prevents a call within the first 30 minutes of the site being up from showing no news.

    @classmethod
    @swagger_auto_schema(operation_id="get_starbase_news", tags=["utils"])
    def get(cls, request):
        cached = True
        if time.time() - cls.time_since_news_request >= 1800:
            cls.time_since_news_request = time.time()

            cached = False

            api_key = os.getenv('STEAM_API_KEY', '')
            app_id = 454120

            starbase_news_url = f"https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?key={api_key}&format=json&appid={app_id}"
            starbase_news_request = requests.get(starbase_news_url)
            cls.cached_news = starbase_news_request.json()["appnews"]["newsitems"][-1]

        return JsonResponse({'news': cls.cached_news, 'cached': cached})
