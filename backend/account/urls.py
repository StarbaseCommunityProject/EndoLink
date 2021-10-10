from django.urls import path, include

from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView

from . import views


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('current_user/', views.CurrentUserView.as_view(), name='current_user'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('', include('django.contrib.auth.urls')),  # Default Django auth module.
    # path('signup', views.signup, name='signup'),
    # path('', views.account_page, name='account'),
    # path('account/edit', views.account_edit_page, name='edit')
]
]
