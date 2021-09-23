from django.contrib import admin
from .models import Faction, FactionRole, FactionMember, FactionEmblem, FactionInvitation, FactionAdvertisement

# Register your models here.


class FactionAdmin(admin.ModelAdmin):
    pass


class FactionRoleAdmin(admin.ModelAdmin):
    pass


class FactionMemberAdmin(admin.ModelAdmin):
    pass


class FactionEmblemAdmin(admin.ModelAdmin):
    pass


class FactionInvitationAdmin(admin.ModelAdmin):
    pass


class FactionAdvertisementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Faction, FactionAdmin)
admin.site.register(FactionRole, FactionRoleAdmin)
admin.site.register(FactionMember, FactionMemberAdmin)
admin.site.register(FactionEmblem, FactionEmblemAdmin)
admin.site.register(FactionInvitation, FactionInvitationAdmin)
admin.site.register(FactionAdvertisement, FactionAdvertisementAdmin)
