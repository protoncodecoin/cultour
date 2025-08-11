from django.utils import timezone
from django.db import models
from places.models import City
from users.models import RestaurantOwner, Tourist
from django.db.models import Avg


from ratings.mixins import RateableModel


# Create your models here.
class Restaurant(RateableModel):
    owner = models.ForeignKey(RestaurantOwner, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to="images/restaurants/")
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    # rating = models.DecimalField(decimal_places=2, max_digits=3)
    notes = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def average_rating(self):
        avg = self.ratings.aggregate(avg=Avg("rating"))["avg"]

        return avg if avg is not None else 0


class RestaurantFood(models.Model):
    FOOD_CATEGORIES = [
        ("main", "Main Course"),
        ("side", "Side Dish"),
        ("drink", "Drink"),
        ("dessert", "Dessert"),
    ]

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=50)
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    image = models.ImageField(upload_to="images/restaurant_food/")
    notes = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=20, choices=FOOD_CATEGORIES, default="main")

    def __str__(self):
        return self.name


class RestaurantTable(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="tables"
    )
    image = models.ImageField(
        upload_to="images/restaurant_tables/",
        default="images/default/default.jpg",
    )
    table_number = models.CharField(max_length=10, unique=True)
    seats = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    fee = models.DecimalField(decimal_places=2, max_digits=50)

    def __str__(self):
        return f"Table {self.table_number} - {self.restaurant.name}"


class TableReservation(models.Model):
    user = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    table = models.ForeignKey(
        RestaurantTable, on_delete=models.CASCADE, related_name="reservations"
    )
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    guests = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    is_paid = models.BooleanField(default=False)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reservation by {self.user.user.username} on {self.reservation_date} at {self.reservation_time}"

    def is_active(self):
        today = timezone.now().date()
        return self.reservation_date <= today
