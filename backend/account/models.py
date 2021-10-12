from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now


# Create your models here.


class UserExtraInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    in_game_name = models.CharField(max_length=100, default="", null=True, blank=True)
    discord_name = models.CharField(max_length=100, default="", null=True, blank=True)
    forum_name = models.CharField(max_length=100, default="", null=True, blank=True)

    bio = models.TextField(max_length=1000, default="", null=True, blank=True)

    home_origin = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)], null=True, blank=True)

    profile_picture = models.ImageField(null=True, blank=True, upload_to='profile_pictures')

    def __str__(self):
        return self.user.username
