from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Flat
from .forms import FlatForm ## TODO


# Create your views here.



# def index(request):
#     context = {
#         'flats': Flat.objects.all()
#     }
#     return render(request, 'airbnb/index.html', context)

# @login_required
# def profile_view(request):
#     user_flats = Flat.objects.filter(owner = request.user.userprofile)
#     context={
#         'user_flats':user_flats
#     }
#     return render(request, 'airbnb/profile.html', context)


## CBVs version of my views

class FlatListView(ListView):
    model = Flat
    template_name = 'airbnb/index.html'
    context_object_name = 'flats'


class ProfileView(LoginRequiredMixin, ListView):
    model = Flat
    template_name = 'airbnb/profile.html'
    context_object_name = 'user_flats'

    def get_queryset(self): 
        return Flat.objects.filter(owner = self.request.user.userprofile)
    


class FlatCreateView(LoginRequiredMixin, CreateView):
    model=Flat
    form_class = FlatForm 
    template_name = 'airbnb/flat_form.html'
    success_url = reverse_lazy('airbnb:profile.html')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user.userprofile
        return super().form_valid(form)

    

class FlatUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model= Flat
    form_class = FlatForm
    template_name = 'airbnb/flat_form.html'
    success_url = reverse_lazy('airbnb:profile.html')

    def test_func(self):
        flat =self.get_object()
        return flat.owner.user == self.request.user

class FlatDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Flat
    template_name = 'airbnb/flat_confirm_delete.html'
    success_url = reverse_lazy('airbnb:profile')

    def test_func(self):
        flat =self.get_object()
        return flat.owner.user == self.request.user

