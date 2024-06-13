from django import forms
from booking.models import Room, Booking, Aviliability

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["user", "room", "start_date", "end_date"]

        widgets = {
            "start_date": forms.DateTimeInput(attrs={"type":"datetime-local"}),
            "end_date": forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }