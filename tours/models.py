from django.contrib.auth.models import User
from django.db import models
from places.models import City
from users.models import Tourist, TourSiteOwner


# Create your models here.
class TourSite(models.Model):
    owner = models.ForeignKey(TourSiteOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="images", blank=True)
    image2 = models.ImageField(upload_to="images", blank=True)
    description = models.TextField()
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tour(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    site = models.ForeignKey(TourSite, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    fee = models.DecimalField(max_digits=50, decimal_places=2)
    notes = models.TextField()
    start_datetime = models.DateField()
    end_datetime = models.DateField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.city.name} -> {self.site.name}"
