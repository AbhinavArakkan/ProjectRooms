from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .services import RoomService, InterviewService
from .serializers import RoomSerializer

class RoomList(APIView):
    def get(self, request, *args, **kwargs):
        rooms = RoomService.get_all_rooms()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            room = RoomService.create_room(serializer.validated_data)
            return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomDetail(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            room = RoomService.get_room(pk)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        try:
            room = RoomService.get_room(pk)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            room = RoomService.update_room(room, serializer.validated_data)
            return Response(RoomSerializer(room).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            room = RoomService.get_room(pk)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        RoomService.delete_room(room)
        return Response(status=status.HTTP_204_NO_CONTENT)

class AssignDirector(APIView):
    def post(self, request, room_id, director_id, *args, **kwargs):
        try:
            InterviewService.assign_director(room_id, director_id)
            return Response({"message": "Director assigned successfully"}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

class ScheduleInterview(APIView):
    def post(self, request, room_id, *args, **kwargs):
        try:
            InterviewService.schedule_interview(room_id)
            return Response({"message": "Interview scheduled successfully"}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
