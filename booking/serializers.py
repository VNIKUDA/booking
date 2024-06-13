from rest_framework import serializers
from booking.models import Booking, Room, Aviliability

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class AvaliabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviliability
        fields = "__all__"