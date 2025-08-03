from django.db import models

from django_countries.fields import CountryField

# Create your models here.
# class Country(models.Model):
#     name = models.CharField(max_length=100)
#     flag = models.ImageField(upload_to="images/", null=True, blank=True)
#     currency = models.CharField(max_length=50)
#     createdon = models.DateTimeField(auto_now_add=True)
#     updatedon = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


class State(models.Model):
    name = models.CharField(max_length=100)
    t_country = CountryField(blank=True)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    createdon = models.DateTimeField(auto_now_add=True)
    updatedon = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
