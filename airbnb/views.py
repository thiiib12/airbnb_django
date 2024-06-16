from django.shortcuts import render
from .models import Flat

# Create your views here.



def index(request):
    context = {
        'flats': Flat.objects.all()
    }
    return render(request, 'airbnb/index.html', context)

