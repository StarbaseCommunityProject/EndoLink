from django.contrib import admin
from .models import UserExtraInfo

# Register your models here.


class UserExtraInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserExtraInfo, UserExtraInfoAdmin)
