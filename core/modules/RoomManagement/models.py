from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    floor_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name

class BoardMember(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=False)
    is_director = models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])
    location = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)
    available_from = models.DateTimeField(null=True, default=None)
    available_to = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return self.name

class InterviewRoom(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='interview_rooms')
    director = models.ForeignKey(BoardMember, on_delete=models.CASCADE, related_name='interview_rooms')
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()
    STATUS_CHOICES = [
        ('Occupied', 'Occupied'),
        ('Available', 'Available'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Interview Room {self.id} - {self.room.room_name}"
