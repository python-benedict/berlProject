from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import DetailedUserForm
from .utils import auto_check_add_user_to_room
from .forms import NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
# Create your views here.

#This is a register function
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            # Here i am saving a user and putting it in a container
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})

# This is a login function
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("detaileduser")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})
	

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("detaileduser")
    	
	 
@login_required
def detaileduser(request):
    form = DetailedUserForm()

    if request.method == "POST":
        form = DetailedUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            # Check for auto room allocation or manual 
            if user.room_choosing_status == DetailedUser.choose_for_me:
                if (auto_check_add_user_to_room(user, request)):
                    messages.success(request, "")
                else:
                    messages.info(request, 'We were not able to find a perfect room for you so manually choose one')
                    return redirect('chooseroom') 
            #Redirecting user to manual room selection page
            else:
                return redirect('chooseroom')   


    context ={
        'form':form
    }
    return render(request, 'detaileduser.html', context)


@login_required
def chooseroom(request):
    rooms = Room.objects.filter(full=False).iterator(chunk_size=50)
    room_members =[]
    if request.method == 'POST':
        selectedRoomId  = request.POST['roomchoose']
        detaileduser    = DetailedUser.objects.get(user=request.user)
        room            = Room.objects.get(id=selectedRoomId)
        room.people.add(detaileduser)
        room_members=room.people.all()
        messages.success(request, "Successfully placed in room %s with" %(room.name))
        # Check and tick room to full 
        if room.people.count() == room.capacity:
            room.full = True 
            room.save()

    context = {
        'room':rooms,
        'room_members':room_members
    }
    return render(request, 'chooseroom.html', context)

