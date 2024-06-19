from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import UserProfile
from faker import Faker
from django.core.files import File
from django.conf import settings
import os
import random
from PIL import Image
import shutil

class Command(BaseCommand):
    help = 'Seed the database with initial user data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clean the media/avatars directory
        media_avatar_path = os.path.join(settings.MEDIA_ROOT, 'avatars')
        if os.path.exists(media_avatar_path):
            shutil.rmtree(media_avatar_path)
        os.makedirs(media_avatar_path)
        
        # Delete all users except superuser
        User.objects.exclude(is_superuser=True).delete()
        
        # Define the path to the avatar images
        path_to_avatar_images = os.path.join(settings.BASE_DIR, 'seed_data/seed_avatars')
        avatar_files = [f for f in os.listdir(path_to_avatar_images) if os.path.isfile(os.path.join(path_to_avatar_images, f))]
        
        # Create 10 fake users
        for _ in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = f"{first_name.lower()}.{last_name.lower()}"
            email = f"{username}@example.com"
            password = 'password123'
            
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            
            # Assign avatar from the list to the automatically created UserProfile
            if avatar_files:
                avatar_file = random.choice(avatar_files)
                avatar_path = os.path.join(path_to_avatar_images, avatar_file)
                profile = user.userprofile  # Access the automatically created UserProfile
                with open(avatar_path, 'rb') as f:
                    img = Image.open(f)
                    if img.mode == 'RGBA':
                        img = img.convert('RGB')
                    # Save the converted image to profile.avatar
                    temp_path = os.path.join(media_avatar_path, f'{username}.jpg')
                    img.save(temp_path, 'JPEG')
                    with open(temp_path, 'rb') as temp_f:
                        profile.avatar.save(f'{username}.jpg', File(temp_f), save=True)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with 10 users.'))
