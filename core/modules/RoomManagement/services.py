from .models import Room, BoardMember, InterviewRoom

class RoomService:
    @staticmethod
    def get_all_rooms():
        return Room.objects.all()

    @staticmethod
    def create_room(data):
        return Room.objects.create(**data)

    @staticmethod
    def get_room(pk):
        return Room.objects.get(pk=pk)

    @staticmethod
    def update_room(room, data):
        for key, value in data.items():
            setattr(room, key, value)
        room.save()
        return room

    @staticmethod
    def delete_room(room):
        room.delete()


class InterviewService:
    @staticmethod
    def schedule_interview(room_id):
        try:
            room = InterviewRoom.objects.get(id=room_id)
        except InterviewRoom.DoesNotExist:
            raise ValueError("Interview room not found")

        # Check if the director is available during the scheduled time
        if not InterviewService.is_director_available(room.director, room.from_time, room.to_time):
            raise ValueError("Director is not available during the scheduled time")


    @staticmethod
    def is_director_available(director, from_time, to_time):
        # Assuming 'available_from' and 'available_to' are in the director model
        available_from = director.available_from
        available_to = director.available_to

        # Check if the director's availability overlaps with the scheduled interview time
        return available_from <= from_time and available_to >= to_time

