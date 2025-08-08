from django.contrib.auth.models import User
from django.db import models
from gallery.models import Media
from places.models import City
from users.models import Tourist, TourSiteOwner
from ratings.mixins import RateableModel

from django.db.models import Avg


# Create your models here.
class TourSite(RateableModel):
    owner = models.ForeignKey(TourSiteOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="images", blank=True)
    image2 = models.ImageField(upload_to="images", blank=True)
    description = models.TextField()
    # rating = models.DecimalField(decimal_places=2, max_digits=3)
    featured_images = models.ManyToManyField(
        Media, blank=True, related_name="featured_image"
    )
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)
    is_top_tour = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def average_rating(self, obj):
        return obj.ratings.aggregate(avg=Avg("rating"))["avg"]

    def calculate_average_rating(self):
        return self.ratings.aggregate(avg=Avg("rating"))["avg"]


class Tour(models.Model):
    site = models.ForeignKey(TourSite, on_delete=models.CASCADE, related_name="tours")
    # city = models.ForeignKey(City, on_delete=models.CASCADE)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    package_image = models.ImageField(
        upload_to="tour/packages/", default="images/default-package.jpeg"
    )
    notes = models.TextField()
    start_datetime = models.DateField()
    end_datetime = models.DateField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.site.name} ({self.start_datetime} to {self.end_datetime} {self.fee})"


class TourReservation(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    guests = models.PositiveIntegerField(default=1)
    is_paid = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tourist.user.username} booking for {self.tour.site.name}"
