from django.http import JsonResponse
from .models import Showtime

def session_seats(request, id):
    showtime = Showtime.objects.get(id=id)
    return JsonResponse({
        "showtime": showtime.id,
        "movie": showtime.movie.title,
        "hall": showtime.hall.name,
    })
