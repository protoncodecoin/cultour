# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from hotels.models import HotelReservation
from payment.api.serializers import PaymentSerializer
from payment.models import Payment
from .serializers import HotelReservationSerializer


class HotelReservationAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = HotelReservationSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            amount = serializer.validated_data.pop("amount")
            reservation = serializer.save()
            # Create a related payment instance
            amount = HotelReservation.calculate_reservation_amount(reservation)
            content_type = Payment.get_content_type("HotelReservation")
            payment = Payment.objects.create(
                user=request.user.tourist,
                amount=amount,
                content_type=content_type,
                object_id=reservation.pk,
            )

            # Serialize the payment object
            payment_data = PaymentSerializer(payment).data
            payment_data["amount"] = payment_data["amount"] * 100  # type: ignore

            return Response(payment_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
