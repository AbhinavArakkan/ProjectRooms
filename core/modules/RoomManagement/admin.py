from django.contrib import admin
from .models import Room, BoardMember, InterviewRoom

# Register your models here.
admin.site.register(Room)
admin.site.register(BoardMember)
admin.site.register(InterviewRoom)
