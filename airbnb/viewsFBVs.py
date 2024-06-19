from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from crispy_forms.helper import FormHelper
from .models import Flat
from .forms import FlatForm
from django.http import HttpResponseForbidden


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

def flat_form_view(request, flat_id = None):
    if flat_id:
        flat = get_object_or_404(Flat, id = flat_id)
        if flat.owner.user != request.user:
            return render(request, 'airbnb/errors.html', {'error_message': "You are not allowed to edit this flat."})
    else:
        flat = None
    
    if request.method =='POST':
        form = FlatForm(request.POST, request.FILES, instance = flat)
        if form.is_valid():
            flat = form.save(commit = False)
            flat.owner = request.user.userprofile
            flat.save()
            return redirect('/profile')
    else:
        form = FlatForm(instance=flat)


    helper = FormHelper(form)
    helper.form_method = 'post'

    context = {
        'flat':flat,
        'form':form,
        'helper': helper
    }

    return render(request, 'airbnb/flat_form.html', context)





def flat_delete(request, flat_id=None):
    flat = get_object_or_404(Flat, id = flat_id)

    if flat.owner.user != request.user:
        return render(request, 'airbnb/errors.html', {'error_message': "You are not allowed to delete this flat."})
    
    if request.method == 'POST':
        flat.delete()
    return redirect('airbnb:profile')
