from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, ValidationError
from django.utils.timezone import now

# Create your models here.


class ShipImage(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='ship_images')
    description = models.CharField(max_length=150, default="", null=True, blank=True)


class ShipEntry(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_ship')
    ship_name = models.CharField(max_length=150, default="", null=False, blank=False)
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

    like_users = models.ManyToManyField(User, through='ShipLike', related_name='liked_ship')
    wishlist_users = models.ManyToManyField(User, through='ShipWishlist', related_name='whitelisted_ship')

    @property
    def likes(self):
        return self.shiplike_set.count()

    def clean(self):
        """
        Ran upon validation by a ModelForm. Not called during a .save()!
        """
        super().clean()
        if self.price is None and self.price_blueprint is None:
            raise ValidationError('Ship price and blueprint price are both None')


class ShipLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_ship = models.ForeignKey(ShipEntry, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(default=now, null=False, blank=False)

    class Meta:
        unique_together = ('user', 'liked_ship')


class ShipWishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wishlisted_ship = models.ForeignKey(ShipEntry, on_delete=models.CASCADE)
    wishlisted_at = models.DateTimeField(default=now, null=False, blank=False)

    class Meta:
        unique_together = ('user', 'wishlisted_ship')
