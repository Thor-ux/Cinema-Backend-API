from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CinemaHall, Seat
from .serializers import HallSerializer, SeatSerializer
from users.permissions import IsAdmin

class HallAdminViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [IsAdmin]

@api_view(['GET'])
def hall_seats(request, hall_id):
    seats = Seat.objects.filter(hall_id=hall_id)
    return Response(SeatSerializer(seats, many=True).data)
