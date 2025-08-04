from django.db import models
from django.utils.translation import gettext_lazy as _

from places.models import City
from users.models import FestivalOwner
from gallery.models import Media


# Create your models here.
class Festival(models.Model):

    class Month(models.TextChoices):
        JANUARY = "January", _("January")
        FEBRUARY = "February", _("February")
        MARCH = "March", _("March")
        APRIL = "April", _("April")
        MAY = "May", _("May")
        JUNE = "June", _("June")
        JULY = "July", _("July")
        AUGUST = "August", _("August")
        SEPTEMBER = "September", _("September")
        OCTOBER = "October", _("October")
        NOVEMBER = "November", _("November")
        DECEMBER = "December", _("December")

    CATEGORY_CHOICES = [
        ("cultural", "Cultural"),
        ("religious", "Religious"),
        ("music", "Music"),
        ("harvest", "Harvest"),
        ("other", "Other"),
    ]

    owner = models.ForeignKey(FestivalOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    history = models.TextField()
    month_of_celebration = models.CharField(
        max_length=20,
        choices=Month.choices,
        default=Month.JANUARY,
    )
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="cultural"
    )
    cover_image = models.ImageField(upload_to="festival_covers/", null=True, blank=True)
    gallery = models.ManyToManyField(Media, blank=True, related_name="festivals")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    creatdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
