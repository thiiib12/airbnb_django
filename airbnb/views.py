from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Flat

# Create your views here.



def index(request):
    context = {
        'flats': Flat.objects.all()
    }
    return render(request, 'airbnb/index.html', context)

@login_required
def profile_view(request):
    user_flats = Flat.objects.filter(owner = request.user.userprofile)
    context={
        'user_flats':user_flats
    }
    return render(request, 'airbnb/profile.html', context)

