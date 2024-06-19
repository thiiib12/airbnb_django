# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='home'),
#     path('profile/', views.profile_view, name='profile'),
# ]



from django.urls import path
from .views import FlatListView, FlatCreateView, FlatUpdateView, FlatDeleteView, ProfileView

app_name = 'airbnb'

urlpatterns = [
    path('', FlatListView.as_view(), name='flat_list'),
    path('flat/new/', FlatCreateView.as_view(), name='flat_create'),
    path('flat/<int:pk>/edit/', FlatUpdateView.as_view(), name='flat_edit'),
    path('flat/<int:pk>/delete/', FlatDeleteView.as_view(), name='flat_delete'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
