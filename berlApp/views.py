from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import DetailedUserForm
from .utils import auto_check_add_user_to_room
# Create your views here.
def detaileduser(request):
    form = DetailedUserForm()

    if request.method == "POST":
        form = DetailedUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Check for auto room allocation or manual 
            if user.room_choosing_status == DetailedUser.choose_for_me:
                if (auto_check_add_user_to_room(user)):
                    messages.success(request, "Successfully allocated to a room")
                else:
                    messages.info(request, 'We were not able to find a perfect room for you so manually choose one')
                    return redirect('chooseroom') 
            #Redirecting user to manual room selection page
            else:
                pass   


    context ={
        'form':form
    }
    return render(request, 'detaileduser.html', context)

def chooseroom(request):
    rooms = Room.objects.filter(full=False).iterator(chunk_size=50)
    context={'room':rooms}
    if request.method == 'POST':
        roomchoose = request.POST['roomchoose']
    return render(request, 'chooseroom.html', context)
