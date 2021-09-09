from django.contrib import admin
from .models import ShipEntry, ShipImage, ShipLike

# Register your models here.


class ShipEntryAdmin(admin.ModelAdmin):
    pass


class ShipImageAdmin(admin.ModelAdmin):
    pass


class ShipLikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShipEntry, ShipEntryAdmin)
admin.site.register(ShipImage, ShipImageAdmin)
admin.site.register(ShipLike, ShipLikeAdmin)
