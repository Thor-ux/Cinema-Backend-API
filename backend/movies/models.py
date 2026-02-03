from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    base_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True 
    )

    release_date = models.DateField(
        null=True,
        blank=True
    )

def __str__(self):
        return self.title