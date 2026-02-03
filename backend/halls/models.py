from django.db import models

class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.PositiveIntegerField()
    seats_per_row = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Seat(models.Model):
    SEAT_TYPES = (
        ('VIP', 'VIP'),
        ('REGULAR', 'Regular'),
    )

    hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, related_name="seats")
    row_number = models.PositiveIntegerField()
    seat_number = models.PositiveIntegerField()
    seat_type = models.CharField(max_length=10, choices=SEAT_TYPES)

    class Meta:
        unique_together = ('hall', 'row_number', 'seat_number')
