from django.urls import path, include, reverse
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from booking.views import BookingViewSet, AviliabilityViewSet, RoomViewSet, BookingFormView, index

router = DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('bookings', BookingViewSet)
router.register('aviliablitity', AviliabilityViewSet)

urlpatterns = [
    path("", index, name="index"),
    path("", include(router.urls)),
    path("book/",login_required(BookingFormView.as_view(), login_url="/user/login"), name="booking_form")
]

# urlpatterns = [
#     path("", booking_views.room_list, name="room_list"),
#     path("<int:room_id>", booking_views.room_details, name="room_details")
# ]
