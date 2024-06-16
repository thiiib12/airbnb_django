from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'user profiles'
    fields = ('avatar', 'avatar_thumbnail')

    readonly_fields = ('avatar_thumbnail',)

    def avatar_thumbnail(self, instance):
        if instance.avatar:
            return f'<img src="{instance.avatar.url}" width="50" height="50" />'
        return "No Avatar"
    avatar_thumbnail.allow_tags = True
    avatar_thumbnail.short_description = 'Avatar Thumbnail'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
