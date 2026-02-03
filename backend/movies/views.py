from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer
