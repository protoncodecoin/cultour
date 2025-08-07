# serializers.py
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    content_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.all(), slug_field="model"
    )

    class Meta:
        model = Payment
        fields = [
            "id",
            "user",
            "amount",
            "ref",
            "verified",
            "content_type",
            "object_id",
            "date_created",
        ]
        read_only_fields = ["verified", "date_created"]


class VerifyPaymentSerializer(serializers.Serializer):
    content_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.all(), slug_field="model"
    )
    # amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    ref = serializers.CharField()
    object_id = serializers.IntegerField()
