from django.shortcuts import render
from .models import *
# Create your views here.
def detailedUser(request):
    if request.method == 'POST':
        fullname    = request.POST['fullname']
        email       = request.POST['email']
        studentId   = request.POST['studentId']
        gender      = request.POST['gender']
        roomtype    = request.POST['roomtype']
        room_choosing_status = request.POST['room_choosing_status']
        bio         = request.POST['bio']
        detaileduser = DetailedUser.objects.create(fullname=fullname, email=email, studentId=studentId, gender=gender, roomtype=roomtype, room_choosing_status=room_choosing_status, bio=bio)
        if DetailedUser.objects.filter(roomtype='FOUR IN A ROOM SELF-CONTAIN WITH BALCONY KICHENNETTE'):
            MRoom1mw.name.add(detaileduser)
    return render(request, 'detaileduser.html')