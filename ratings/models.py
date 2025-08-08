from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

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
        )

    @classmethod
    def create_for(cls, *, user, obj, rating, comment=None):

        if not hasattr(obj, "ratings"):
            raise TypeError("This object cannot be rated. Add the RateableModel mixin.")

        content_type = ContentType.objects.get_for_model(obj.__class__)
        return cls.objects.create(
            user=user,
            rating=rating,
            comment=comment,
            content_type=content_type,
            object_id=obj.id,
        )
