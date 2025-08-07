from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from payment.api.serializers import PaymentSerializer
from payment.models import Payment
from tours.api.serializers import TourReservationSerializer
from tours.models import TourReservation


class TourReservationView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def post(self, request):
        print(request.data)
        serializer = TourReservationSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data.pop("amount")

            reservation = serializer.save()

            # create a related payment instance
            content_type = Payment.get_content_type("TourReservation")
            payment = Payment.objects.create(
                user=request.user.tourist,
                amount=amount,
                content_type=content_type,
                object_id=reservation.pk,
            )

            # serialize the payment object
            payment_data = PaymentSerializer(payment).data
            payment_data["amount"] = payment_data["amount"] * 100  # type: ignore

            return Response(payment_data, status=status.HTTP_201_CREATED)

        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
