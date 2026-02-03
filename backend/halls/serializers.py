from rest_framework import serializers
from .models import CinemaHall, Seat

class SeatSerializer(serializers.ModelSerializer):
    is_booked = serializers.SerializerMethodField()

    class Meta:
        model = Seat
        fields = '__all__'

    def get_is_booked(self, obj):
        return obj.ticket_set.exists()

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = '__all__'
