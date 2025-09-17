# models/mixins.py

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from .models import Rating


class RateableModel(models.Model):
    ratings = GenericRelation(Rating)

    class Meta:
        abstract = True
        # ordering = []
