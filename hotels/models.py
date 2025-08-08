from django.db import models
from gallery.models import Media
from places.models import City
from users.models import HotelOwner, Tourist
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from ratings.models import Rating
from django.db.models import Avg

from ratings.mixins import RateableModel


# Create your models here.
class Hotel(RateableModel):
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
    notes = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def calculate_average_rating(self):
        return self.ratings.aggregate(avg=Avg("rating"))["avg"]

    # def average_rating(self, obj):
    #     return obj.ratings.aggregate(avg=Avg("rating"))["avg"]


class HotelRoom(RateableModel):

    ROOM_TYPE_CHOICES = [
        ("single", "Single"),
        ("double", "Double"),
        ("suite", "Suite"),
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.TextField()
    fee = models.DecimalField(decimal_places=2, max_digits=50)
    notes = models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(
        max_length=20, choices=ROOM_TYPE_CHOICES, default="single"
    )
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="hotel_rooms/")
    featured_images = models.ManyToManyField(
        Media, blank=True, related_name="hotel_rooms"
    )

    def __str__(self):
        return self.name

    def average_rating(self, obj):
        return obj.ratings.aggregate(avg=Avg("rating"))["avg"]


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
        return f"{self.user} - {self.room.name} ({self.check_in} to {self.check_out})"

    def duration(self):
        return (self.check_out - self.check_in).days

    def is_active(self):
        today = timezone.now().date()
        return self.check_in <= today <= self.check_out

    from decimal import Decimal

    @staticmethod
    def calculate_reservation_amount(reservation):
        """
        Calculate the amount to be paid for a hotel reservation.

        Arguments:
            reservation (HotelReservation): The reservation instance.

        Returns:
            Decimal: Total amount for the reservation.
        """
        nights = reservation.duration()

        # Ensure at least 1 night (guard against zero or negative durations)
        if nights <= 0:
            nights = 1

        # Get the room fee (already a Decimal field)
        fee_per_night = reservation.room.fee

        total = fee_per_night * nights

        return total
