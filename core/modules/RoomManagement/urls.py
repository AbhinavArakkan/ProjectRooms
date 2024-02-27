from django.urls import path
from .controllers import RoomList, RoomDetail, AssignDirector, ScheduleInterview

app_name = 'room_management'

urlpatterns = [
    path('rooms/', RoomList.as_view(), name='room-list'),
    path('rooms/<uuid:pk>/', RoomDetail.as_view(), name='room-detail'),
    path('assign-director/<uuid:room_id>/<uuid:director_id>/', AssignDirector.as_view(), name='assign-director'),
    path('schedule-interview/<uuid:room_id>/', ScheduleInterview.as_view(), name='schedule-interview'),
]