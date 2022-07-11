from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def detaileduser(request):
    rooms       = Room.objects.all()

    if request.method == "POST":
        fullName        = request.POST['fullname']
        email           = request.POST['email']
        selectedRoom    = request.POST['roomId']
        studentId       = request.POST['studentId']
        gender          = request.POST['gender']
        room_choosing_status = request.POST['room_choosing_status']
        bio             = request.POST['bio']
        # create user
        detaileduser    = DetailedUser.objects.create(fullName=fullName, email=email, studentId=studentId, gender=gender, room_choosing_status=room_choosing_status, bio=bio)
        
        # add user to room
        room            = get_object_or_404(Room, id=selectedRoom)
        room.bookings.add(detaileduser)

    context ={
        "rooms":rooms
    }
    return render(request, 'detaileduser.html', context)
