from rest_framework import serializers

from tours.models import TourReservation


class TourReservationSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = TourReservation
        fields = "__all__"
        read_only_fields = ["created_on", "amount"]

    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)
