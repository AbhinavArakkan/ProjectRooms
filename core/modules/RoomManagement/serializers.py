from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_name', 'location', 'floor_number', 'created_at']
        
class BoardMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMember
        fields = '__all__'

class InterviewRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewRoom
        fields = '__all__'
