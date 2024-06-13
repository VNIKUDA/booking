# from django.shortcuts import render
# from booking.models import Room, Booking

# # Create your views here.
# def room_list(request):
#     rooms = Room.objects.all()

#     context = {
#         "room_list": rooms
#     }

#     return render(request, "booking/room_list.html", context=context)

# def room_details(request, room_id):
#     room = Room.objects.get(id=room_id)
#     bookings = Booking.objects.filter(room_id = room_id)

#     context = {
#         "room": room,
#         "bookings": bookings
#     }

#     return render(request, "booking/room_details.html", context=context)

from rest_framework import viewsets
from booking.models import Room, Booking, Aviliability
from booking.serializers import RoomSerializer, BookingSerializer, AvaliabilitySerializer
from django.shortcuts import render, redirect
from django.views import View
from booking.forms import BookingForm

class BookingFormView(View):
    def get(self, request):
        form = BookingForm()
        return render(request, "booking/booking_form.html", {"form": form})
    
    def post(self, request):
        form = BookingForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect("booking_form")
        
        return render(request, "booking/booking_form.html", {'form': form})

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class AviliabilityViewSet(viewsets.ModelViewSet):
    queryset = Aviliability.objects.all()
    serializer_class = AvaliabilitySerializer