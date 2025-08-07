from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.conf import settings

from users.models import Tourist


class Rating(models.Model):
    user = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # 1-5 scale
    comment = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            "user",
            "content_type",
            "object_id",
        )  # Prevent duplicate ratings
