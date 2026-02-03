from rest_framework.viewsets import ModelViewSet
from users.permissions import IsAdmin
from .models import Showtime
from .serializers import ShowtimeSerializer

class ShowtimeAdminViewSet(ModelViewSet):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = [IsAdmin]
