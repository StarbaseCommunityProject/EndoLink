from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now

# Create your models here.


class ShipImage(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='ship_images')
    description = models.CharField(max_length=150, default="", null=True, blank=True)


class ShipEntry(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    ship_name = models.CharField(max_length=150, default="", null=True, blank=True)
    description = models.TextField(max_length=6000, default="", null=True, blank=True)
    tags = models.JSONField(default=list, null=True, blank=True)
    attributes = models.JSONField(default=dict, null=True, blank=True)
    images = models.ManyToManyField(ShipImage, blank=True)
    price = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    price_blueprint = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    created_at = models.DateTimeField(default=now, null=False, blank=False)
    updated_at = models.DateTimeField(default=now, null=False, blank=False)
    is_public = models.BooleanField(default=True, null=False, blank=False)
    is_deleted = models.BooleanField(default=False, null=False, blank=False)     # Do we want to delete things; or keep them stored but flagged as deleted?

    @property
    def likes(self):
        return self.shiplike_set.count()


class ShipLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_ship = models.ForeignKey(ShipEntry, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'liked_ship')
