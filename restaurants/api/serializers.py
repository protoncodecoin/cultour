from datetime import datetime
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from restaurants.models import RestaurantTable, TableReservation
from users.models import Tourist

from django.contrib.auth import get_user_model

User = get_user_model()


class TableReservationSerializer(ModelSerializer):
    class Meta:
        model = TableReservation
        fields = ["table", "reservation_date", "reservation_time", "guests"]

    def to_internal_value(self, data):
        data = data.copy()

        # Convert reservation_date from any custom format to YYYY-MM-DD
        date_str = data.get("reservation_date")
        if date_str:
            try:
                # Attempt to parse common wrong formats
                # E.g. MM/DD/YYYY to YYYY-MM-DD
                parsed_date = datetime.strptime(date_str, "%m/%d/%Y")
                data["reservation_date"] = parsed_date.date().isoformat()
            except (ValueError, TypeError):
                pass  # Let default validation handle it if it fails

        # Convert reservation_time from HH:MM AM/PM to 24hr format if needed
        time_str = data.get("reservation_time")
        if time_str:
            try:
                parsed_time = datetime.strptime(time_str, "%I:%M %p")  # 02:30 PM
                data["reservation_time"] = parsed_time.time().isoformat()
            except (ValueError, TypeError):
                pass

        return super().to_internal_value(data)

    def validate(self, attrs):
        user = self.context["request"].user
        user_obj = User.objects.filter(pk=user.pk).first()
        tourist = Tourist.objects.filter(user=user_obj).first()
        # reservation_table = RestaurantTable.objects.get(id=attrs["table"])
        print(attrs["table"])

        if user_obj is None:
            raise serializers.ValidationError("User is not found")

        if tourist is None:
            raise serializers.ValidationError("User profile not found")

        # if reservation_table is None:
        #     raise serializers.ValidationError("Reservation table not found")

        print(user_obj, tourist)
        # attrs["table"] = reservation_table.pk
        attrs["user"] = tourist

        return attrs

    def create(self, validated_data):
        reservation_data = validated_data
        user = self.context["request"].user
        user_obj = User.objects.filter(pk=user.pk).first()
        tourist = Tourist.objects.filter(user=user_obj).first()

        print(user_obj, tourist)
        # reservation_table = RestaurantTable.objects.get(id=validated_data["table"])
        # validated_data["table"] = reservation_table.pk
        # validated_data["user"] = tourist
        print(validated_data)
        table_reservation = TableReservation.objects.create(**reservation_data)
        table_reservation.save()
        return table_reservation
