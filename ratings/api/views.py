from rest_framework import generics, permissions
from ratings.models import Rating
from .serializers import RatingSerializer


class RatingCreateAPIView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]
