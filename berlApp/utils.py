from .models import *
from django.contrib import messages
four_in_a_room = 4
two_in_a_room = 2

def auto_check_add_user_to_room(user, request):
    room_acquired_status = False
    room = Room.objects.filter(roomtype=user.roomtype, gender=user.gender, full=False).first()
    if room:
        room.people.add(user)
        messages.success(request, "Successfully placed in a room %s" %(room.name))
        room_acquired_status = True
        # Check and tick room to full 
        if room.people.count() == room.capacity:
            room.full = True 
            room.save()

    return room_acquired_status