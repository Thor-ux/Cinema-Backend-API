from django.db import models

class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.PositiveIntegerField()
    seats_per_row = models.PositiveIntegerField()

class Seat(models.Model):
    SEAT_TYPES = (
        ('VIP', 'VIP'),
        ('REGULAR', 'Regular'),
    )

    hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    row_number = models.PositiveIntegerField()
    seat_number = models.PositiveIntegerField()
    seat_type = models.CharField(max_length=10, choices=SEAT_TYPES)
