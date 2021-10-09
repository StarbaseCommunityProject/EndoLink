from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
   openapi.Info(
      title="EndoLink API",
      default_version='v1',
      description="This is the EndoLink API",
      contact=openapi.Contact(url="https://discord.gg/qDPF2z6Krh", name="EndoLink developers"),
   ),
   public=True,
   authentication_classes=[JWTAuthentication],
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
