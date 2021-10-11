from django.contrib import admin
from .models import UserExtraInfo
from rest_framework_simplejwt import token_blacklist


# Register your models here.


class UserExtraInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserExtraInfo, UserExtraInfoAdmin)


# The following is a fix for an issue with the rest_framework_simplejwt blacklist app.
# As per: https://github.com/jazzband/djangorestframework-simplejwt/issues/266
class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True


admin.site.unregister(token_blacklist.models.OutstandingToken)
admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)
