from .models import *
four_in_a_room = 4
two_in_a_room = 2

def auto_check_add_user_to_room(user):
    room_acquired_status = False
    for room in Room.objects.filter(roomtype=user.roomtype, gender=user.gender).iterator(chunk_size=50):
        if room.people.count() < room.capacity:
            room.people.add(user)
            room_acquired_status =True
            break

    return room_acquired_status