from django.db import models
from hotels.models import HotelRoom
from restaurants.models import RestaurantFood, Restaurant
from tours.models import Tour
from users.models import Tourist


# Create your models here.
class TourBooking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    notes = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tour.name} -> {self.tourist.name}"


class RoomBooking(models.Model):
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    notes = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.room.name} -> {self.tourist.name}"


class RestaurantOrder(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=2, max_digits=50)
    notes = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.restaurant.name} -> {self.tourist.name}"


class RestaurantOrderFood(models.Model):
    order = models.ForeignKey(RestaurantOrder, on_delete=models.CASCADE)
    food = models.ForeignKey(RestaurantFood, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=50, decimal_places=2)
    notes = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.food.name} -> {self.order}"
