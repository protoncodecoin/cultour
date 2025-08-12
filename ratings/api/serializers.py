# rating/api/serializers.py
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType

from hotels.models import HotelReservation
from restaurants.models import TableReservation
from tours.models import TourReservation
from ..models import Rating


class RatingSerializer(serializers.ModelSerializer):
    model = serializers.CharField(write_only=True)
    object_id = serializers.IntegerField(write_only=True)
    related_model = serializers.CharField(write_only=True)

    class Meta:
        model = Rating
        fields = ["rating", "comment", "model", "related_model", "object_id"]

    def validate(self, data):
        model = data.get("model")
        object_id = data.get("object_id")
        related_model = data.get("related_model")

        try:
            actual_content_type = ContentType.objects.get(model=related_model.lower())
            related_model_class = actual_content_type.model_class()
            obj = related_model_class.objects.get(id=object_id)

            # Hotel, Restaurant, Tour
            content_type = ContentType.objects.get(model=model.lower())
            model_class = content_type.model_class()

            # print("actual: ", actual_content_type, related_model, related_model_class)

            # print("model: ", model_class, content_type, object_id)

            if isinstance(obj, TableReservation):
                # restaurant
                obj = obj.table.restaurant.pk

            if isinstance(obj, HotelReservation):
                obj = obj.hotel.pk

            if isinstance(obj, TourReservation):
                obj = obj.tour.site.pk

        except ContentType.DoesNotExist:
            raise serializers.ValidationError("Invalid model type.")
        except model_class.DoesNotExist:
            raise serializers.ValidationError(
                "Object with the given ID does not exist."
            )

        data["content_type"] = content_type
        data["content_object"] = obj
        return data

    def create(self, validated_data):
        user = self.context["request"].user.tourist
        return Rating.objects.create(
            user=user,
            rating=validated_data["rating"],
            comment=validated_data.get("comment"),
            content_type=validated_data["content_type"],
            object_id=validated_data["object_id"],
        )
