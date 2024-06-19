from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from crispy_forms.helper import FormHelper
from .forms import CustomUserCreationForm
from PIL import Image ## import to resize and avoid too large files


def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('airbnb:flat_list')
    else:
        form = AuthenticationForm(request)

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('airbnb:flat_list')



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('airbnb:flat_list')
    else:
        form = CustomUserCreationForm()

    helper = FormHelper(form)
    helper.form_method = 'post'

    context = {'form': form, 'helper': helper}
    return render(request, 'accounts/register.html', context)
