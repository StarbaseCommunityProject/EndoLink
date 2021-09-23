from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, ValidationError
from django.utils.timezone import now

# Create your models here.


class FactionEmblem(models.Model):
    # TODO: Add foreign key to faction + cascade?
    image = models.ImageField(null=False, blank=False, upload_to='faction_emblems')


class FactionAdvertisement(models.Model):
    # TODO: Potentially make 2 advertisement versions? 1 for web, 1 for Discord?
    # TODO: Add foreign key to faction + cascade?
    image = models.ImageField(null=False, blank=False, upload_to='faction_advertisements')
    description = models.TextField(max_length=4096, null=True, blank=True)
    message = models.TextField(max_length=2000, null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)
    is_embed = models.BooleanField(default=False, null=False, blank=False)


class FactionRole(models.Model):
    # TODO: Add foreign key to faction + cascade?
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Faction(models.Model):
    leader = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leading_faction')
    members = models.ManyToManyField(User, through='FactionMember', blank=True, related_name='member_of_faction')
    invitations = models.ManyToManyField(User, through='FactionInvitation', through_fields=['faction', 'user'], blank=True, related_name='invited_to_faction')
    roles = models.ManyToManyField(FactionRole, blank=True)
    name = models.CharField(max_length=255, default="", null=False, blank=False)
    description = models.TextField(max_length=20000, default="", null=True, blank=True)
    tags = models.JSONField(default=list, null=True, blank=True)
    emblem = models.OneToOneField(FactionEmblem, null=True, blank=True, on_delete=models.SET_NULL)
    advertisement = models.OneToOneField(FactionAdvertisement, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=now, null=False, blank=False)
    updated_at = models.DateTimeField(default=now, null=False, blank=False)
    is_public = models.BooleanField(default=True, null=False, blank=False)
    is_deleted = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"


class FactionMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(default=now, null=False, blank=False)
    roles = models.ManyToManyField(FactionRole, blank=True)

    def __str__(self):
        return f"{self.user.username}"


class FactionInvitation(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='faction_invitation')
    faction = models.ForeignKey(Faction, null=False, blank=False, on_delete=models.CASCADE)
    invited_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='sent_faction_invitation')
    invited_at = models.DateTimeField(default=now, null=False, blank=False)

    def __str__(self):
        return f"{self.user.username}"
