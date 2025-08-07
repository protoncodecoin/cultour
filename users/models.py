from django.contrib.auth.models import User
from django.db import models

from django_countries.fields import CountryField


# Create your models here.
class Tourist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    t_country = CountryField(blank=True)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


# Create your models here.
class TourSiteOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    # country = models.ForeignKey(C, on_delete=models.CASCADE)
    t_country = CountryField(blank=True)

    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


# Create your models here.
class HotelOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    t_country = CountryField(blank=True)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class RestaurantOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    t_country = CountryField(blank=True)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class FestivalOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    country = CountryField(blank=True)
    createdon = models.DateField(auto_now_add=True)
    updatedon = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username
