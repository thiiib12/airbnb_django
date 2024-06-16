from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.size[0] > 1024 or img.size[1] > 1024:
                img.thumbnail((1024, 1024))
            img.save(self.avatar.path, quality=85, optimize=True)