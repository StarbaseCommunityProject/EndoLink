# from django.shortcuts import render, redirect
# from django.http import HttpResponse, JsonResponse
# import json
# # from .forms import SignUpForm, AccountEditForm
# from .models import UserExtraInfo
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import ObjectDoesNotExist
# from django.http import JsonResponse
# from django.views.generic import View

from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from .serializers import UserSerializer, RegisterSerializer


# Create your views here.


class CurrentUserView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            user = request.user
        except Exception as e:
            return Response(None)
        return Response(UserSerializer(user, context={'request': request}).data)


class RegisterView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'register'

    def post(self, request):
        serialiser = RegisterSerializer(data=request.data)
        response = dict()

        if serialiser.is_valid():
            new_user = serialiser.save()
            refresh_token = RefreshToken.for_user(new_user)
            response['jwt'] = {'refresh': refresh_token, 'access': refresh_token.access_token}
            response['user'] = UserSerializer(new_user).data
        else:
            response = serialiser.errors

        return Response(response)


# class SignupView(View):
#     def post(self, request):
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('index')
#         return HttpResponse(render(request, 'account/signup.html', {'form': form}))


# @login_required
# def account_page(request):
#     try:
#         user_extra_info = request.user.userextrainfo
#     except ObjectDoesNotExist:
#         user_extra_info = UserExtraInfo(user=request.user)
#         user_extra_info.save()
#
#     form = AccountEditForm(request.POST or None, instance=user_extra_info)
#
#     if form.is_valid() and request.POST:
#         extra_user_info = form.save(commit=False)
#         extra_user_info.user = request.user
#         profile_picture = request.FILES.get('profile_picture')
#         if profile_picture:
#             extra_user_info.profile_picture = profile_picture
#         extra_user_info.save()
#         return redirect('/account')
#
#     return HttpResponse(render(request, 'account/account_page.html', {'form': form}))
