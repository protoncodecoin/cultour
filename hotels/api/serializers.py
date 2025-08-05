# serializers.py
from rest_framework import serializers
from hotels.models import HotelReservation
from users.models import Tourist


class HotelReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelReservation
        fields = "__all__"
        read_only_fields = ["user", "createdon", "updatedon"]

    def validate(self, data):
        room = data.get("room")
        check_in = data.get("check_in_date")
        check_out = data.get("check_out_date")

        if check_out <= check_in:
            raise serializers.ValidationError("Check-out must be after check-in.")

        overlapping = HotelReservation.objects.filter(
            room=room,
            check_in_date__lt=check_out,
            check_out_date__gt=check_in,
        )
        if overlapping.exists():
            raise serializers.ValidationError("Room is already booked for these dates.")

        user = self.context["request"].user
        tourist = Tourist.objects.filter(user=user).first()

        if tourist is None:
            raise serializers.ValidationError("User Profile not found")

        data["user"] = tourist

        return data
