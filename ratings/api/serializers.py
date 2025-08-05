# ratings/api/serializers.py
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from ratings.models import Rating
from users.models import Tourist


class RatingSerializer(serializers.ModelSerializer):
    model = serializers.CharField(write_only=True)
    object_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Rating
        fields = ["model", "object_id", "rating", "comment"]

    def validate(self, attrs):
        user = self.context["request"].user
        tourist = Tourist.objects.filter(user=user).first()
        if tourist is None:
            raise serializers.ValidationError("User profile not found")

        attrs["user"] = tourist

        return attrs

    def create(self, validated_data):
        model_name = validated_data.pop("model")
        object_id = validated_data.pop("object_id")

        try:
            content_type = ContentType.objects.get(model=model_name.lower())
        except ContentType.DoesNotExist:
            raise serializers.ValidationError({"model": "Invalid model name."})

        rating, created = Rating.objects.update_or_create(
            content_type=content_type,
            object_id=object_id,
            defaults={**validated_data},
        )

        return rating
