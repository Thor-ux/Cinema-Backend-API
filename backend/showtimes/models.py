from django.db import models
from movies.models import Movie
from halls.models import CinemaHall

class Showtime(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="showtimes"
    )
    hall = models.ForeignKey(
        CinemaHall,
        on_delete=models.CASCADE,
        related_name="showtimes"
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price_regular = models.DecimalField(max_digits=6, decimal_places=2)
    price_vip = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.movie.title} | {self.hall.name} | {self.start_time}"
