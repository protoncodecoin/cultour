from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.contenttypes.models import ContentType


from hotels.models import HotelReservation
from payment.api.serializers import PaymentSerializer, VerifyPaymentSerializer
from payment.models import Payment
from restaurants.models import TableReservation
from tours.models import TourReservation


class VerifyPayment(APIView):

    def post(self, request):
        print(request.data)

        serializer = VerifyPaymentSerializer(data=request.data)

        if serializer.is_valid():
            payment_data = serializer.validated_data
            payment = Payment.objects.get(ref=payment_data["ref"])
            verified = payment.verify_payment()

            if verified:
                # check the content  type
                hotel_ct = ContentType.objects.get_for_model(HotelReservation)
                if payment_data["content_type"] == hotel_ct:
                    hotel_reservation_obj = HotelReservation.objects.get(
                        pk=payment_data["object_id"]
                    )
                    print("hotel reservation", hotel_reservation_obj)
                    hotel_reservation_obj.status = "completed"
                    hotel_reservation_obj.save()
                    print("update successful`")
                    return Response(
                        data={"message": "successfully booked hotel"},
                        status=status.HTTP_201_CREATED,
                    )

                tour_ct = ContentType.objects.get_for_model(TourReservation)
                if payment_data["content_type"] == tour_ct:
                    tour_reservation_obj = TourReservation.objects.get(
                        pk=payment_data["object_id"]
                    )
                    tour_reservation_obj.is_paid = True
                    tour_reservation_obj.save()
                    return Response(
                        data={"message": "successfully booked tour"},
                        status=status.HTTP_201_CREATED,
                    )

                table_ct = ContentType.objects.get_for_model(TableReservation)

                if payment_data["content_type"] == table_ct:
                    restaurant_reserve_obj = TableReservation.objects.get(
                        pk=payment_data["object_id"]
                    )
                    restaurant_reserve_obj.is_paid = True
                    restaurant_reserve_obj.save()
                    return Response(
                        data={"message": "table has been successfully reserved"},
                        status=status.HTTP_201_CREATED,
                    )

            print(serializer.errors)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
