from django.db import models
from places.models import City
from users.models import RestaurantOwner


# Create your models here.
class Restaurant(models.Model):
    owner = models.ForeignKey(RestaurantOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    notes = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class RestaurantFood(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=50)
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    notes = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

