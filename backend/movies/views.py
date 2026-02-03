from django.shortcuts import render, get_object_or_404
from .models import Movie
from showtimes.models import Showtime

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "movies/movie_list.html", {"movies": movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    showtimes = Showtime.objects.filter(movie=movie).order_by("start_time")
    return render(
        request,
        "movies/movie_detail.html",
        {
            "movie": movie,
            "showtimes": showtimes,
        }
    )
