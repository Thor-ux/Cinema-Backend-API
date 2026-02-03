from rest_framework import serializers
from .models import Showtime
from showtimes.models import Session

class ShowtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showtime
        fields = '__all__'
