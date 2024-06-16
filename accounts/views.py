from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from crispy_forms.helper import FormHelper
from .forms import CustomUserCreationForm
from PIL import Image ## import to resize and avoid too large files
import pdb


# Create your views here.


def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/login/')
    else:
        form = AuthenticationForm(request)

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/login/')

    # if request.method =='POST':
    #     logout(request)
    #     return redirect("/login/")
    #return render(request, 'accounts/logout.html', {})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = CustomUserCreationForm()

    helper = FormHelper(form)
    helper.form_method = 'post'

    context = {'form': form, 'helper': helper}
    return render(request, 'accounts/register.html', context)


# Comment it to put this logic in the save
# def resize_image(image_path, output_size=(200,200)):
#     with Image.open(image_path) as img:
#         img.thumbnail(output_size)
#         img.save(image_path)