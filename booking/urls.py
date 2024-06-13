from django.urls import path, include
from rest_framework.routers import DefaultRouter
from booking.views import BookingViewSet, AviliabilityViewSet, RoomViewSet, BookingFormView

router = DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('bookings', BookingViewSet)
router.register('aviliablitity', AviliabilityViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("book/", BookingFormView.as_view(), name="booking_form")
]

# urlpatterns = [
#     path("", booking_views.room_list, name="room_list"),
#     path("<int:room_id>", booking_views.room_details, name="room_details")
# ]
