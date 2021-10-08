# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .forms import SignUpForm, AccountEditForm
# from .models import UserExtraInfo
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import ObjectDoesNotExist
# from django.http import JsonResponse
# from django.views.generic import View

# Create your views here.


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
