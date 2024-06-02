from django.urls import path
import booking.views as booking_views

urlpatterns = [
    path("", booking_views.room_list, name="room_list"),
    path("<int:room_id>", booking_views.room_details, name="room_details")
]