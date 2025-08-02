from django.contrib.auth.models import User
from django.db import models
from places.models import Country


# Create your models here.
class Tourist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


# Create your models here.
class TourSiteOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


# Create your models here.
class HotelOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class RestaurantOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
