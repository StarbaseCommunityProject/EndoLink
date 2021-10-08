"""StarbaseCommunityWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from account.router import router as account_router
from factions.router import router as factions_router
from shipshop.router import router as shipshop_router

router = routers.DefaultRouter()

router.registry.extend(account_router.registry)
router.registry.extend(factions_router.registry)
router.registry.extend(shipshop_router.registry)

urlpatterns = [
    path('api/', include('index.urls')),
    path('api/', include('account.urls')),
    path('api/', include('shipshop.urls')),
    path('api/', include('factions.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
