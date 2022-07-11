from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import DetailedUserForm
# Create your views here.
def detaileduser(request):
    rooms       = Room.objects.all()

    if request.method == "POST":
        form = DetailedUserForm(request.POST)
        if form.is_valid():
            form.save()
        

    return render(request, 'detaileduser.html')
