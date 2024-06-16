from django.contrib import admin
from .models import Flat
from accounts.models import UserProfile

class FlatInline(admin.TabularInline):
    model = Flat
    extra = 1

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [FlatInline]

admin.site.register(UserProfile, UserProfileAdmin)

class FlatAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'city', 'country')
    search_fields = ('name', 'owner__username', 'city', 'country')

admin.site.register(Flat, FlatAdmin)
