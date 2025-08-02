from django.db import models
from places.models import City
from users.models import HotelOwner


# Create your models here.
class Hotel(models.Model):
    owner = models.ForeignKey(HotelOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField()
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    notes = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class HotelRoom(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.TextField()
    fee = models.DecimalField(decimal_places=2, max_digits=50)
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    notes = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name