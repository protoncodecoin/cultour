# serializers.py
from rest_framework import serializers
from hotels.models import HotelReservation
from payment.models import Payment
from users.models import Tourist

from datetime import datetime


class HotelReservationSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = HotelReservation
        fields = [
            "user",
            "created_on",
            "updated_on",
            "hotel",
            "room",
            "guests",
            "check_in",
            "check_out",
            "special_requests",
            "amount",
        ]
        read_only_fields = ["user", "createdon", "updatedon"]

    def to_internal_value(self, data):
        data = data.copy()

        # Convert checK_in_date from any custom format to YYYY-MM-DD
        date_str = data.get("check_in")
        if date_str:
            try:
                # Attempt to parse common wrong formats
                # E.g. MM/DD/YYYY to YYYY-MM-DD
                parsed_date = datetime.strptime(date_str, "%m/%d/%Y")
                data["reservation_date"] = parsed_date.date().isoformat()
            except (ValueError, TypeError):
                pass  # Let default validation handle it if it fails

        # Convert check_out_date from HH:MM AM/PM to 24hr format
        time_str = data.get("check_out")
        if time_str:
            try:
                parsed_time = datetime.strptime(time_str, "%I:%M %p")  # 02:30 PM
                data["reservation_time"] = parsed_time.time().isoformat()
            except (ValueError, TypeError):
                pass

        return super().to_internal_value(data)

    def validate(self, data):
        room = data.get("room")
        check_in = data.get("check_in")
        check_out = data.get("check_out")

        if check_out <= check_in:
            raise serializers.ValidationError("Check-out must be after check-in.")

        overlapping = HotelReservation.objects.filter(
            room=room,
            check_in__lt=check_out,
            check_out__gt=check_in,
        )
        if overlapping.exists():
            raise serializers.ValidationError("Room is already booked for these dates.")

        user = self.context["request"].user
        tourist = Tourist.objects.filter(user=user).first()

        if tourist is None:
            raise serializers.ValidationError("User Profile not found")

        data["user"] = tourist
        data["status"] = "completed"

        return data
