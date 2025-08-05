from django.db import models
from gallery.models import Media
from places.models import City
from users.models import HotelOwner, Tourist
from django.utils import timezone


# Create your models here.
class Hotel(models.Model):
    owner = models.ForeignKey(HotelOwner, on_delete=models.CASCADE)
    cover_image = models.ImageField(
        upload_to="hotel/images",
        default="mediafiles/default/default_hotel.jpg",
    )
    featured_images = models.ManyToManyField(
        Media,
        blank=True,
        related_name="featured_images",
    )
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField()
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    notes = models.TextField()
    short_description = models.CharField(default="This is a hotel")
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class HotelRoom(models.Model):

    ROOM_TYPE_CHOICES = [
        ("single", "Single"),
        ("double", "Double"),
        ("suite", "Suite"),
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.TextField()
    fee = models.DecimalField(decimal_places=2, max_digits=50)
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    notes = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(
        max_length=20, choices=ROOM_TYPE_CHOICES, default="single"
    )
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="hotel_rooms/", blank=True, null=True)
    featured_images = models.ManyToManyField(
        Media, blank=True, related_name="hotel_rooms"
    )

    def __str__(self):
        return self.name


class HotelReservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
    ]

    user = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    hotel = models.ForeignKey(
        "Hotel", on_delete=models.CASCADE, related_name="reservations"
    )
    room = models.ForeignKey(
        "HotelRoom", on_delete=models.CASCADE, related_name="reservations"
    )
    guests = models.PositiveIntegerField(default=1)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    special_requests = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
        unique_together = ["room", "check_in", "check_out"]

    def __str__(self):
        return f"{self.user.username} - {self.room.name} ({self.check_in} to {self.check_out})"

    def duration(self):
        return (self.check_out - self.check_in).days

    def is_active(self):
        today = timezone.now().date()
        return self.check_in <= today <= self.check_out
