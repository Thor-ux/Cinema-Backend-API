import uuid
from django.db import models
from movies.models import Movie
from halls.models import CinemaHall, Seat


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price_regular = models.DecimalField(max_digits=6, decimal_places=2)
    price_vip = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.movie.title} | {self.hall.name} | {self.start_time}"


class Ticket(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_code = models.UUIDField(default=uuid.uuid4, unique=True)
    qr_code = models.ImageField(upload_to='qr_codes/')

    def __str__(self):
        return str(self.booking_code)
