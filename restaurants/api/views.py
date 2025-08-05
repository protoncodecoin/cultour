from rest_framework.views import APIView

from hotels.models import Hotel
from restaurants.api.serializers import TableReservationSerializer
from restaurants.models import TableReservation
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class CreateTableReservation(APIView):
    queryset = TableReservation.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = TableReservationSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateHotelReservation(APIView):
    queryset = Hotel.objects.all()
    permission_classes = [IsAuthenticated]
