from django.db import models


# Create your models here.
class Media(models.Model):
    image = models.ImageField(upload_to="festival_images/")
    caption = models.CharField(max_length=255, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption or self.image.name

    # class Meta:
    #     ordering = ["-created_on"]


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=2555, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.caption or }"

    class Meta:
        ordering = ["-created_on"]
