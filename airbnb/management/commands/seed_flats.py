import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.files import File
from faker import Faker
from accounts.models import UserProfile
from airbnb.models import Flat
from django.conf import settings
import random

# Nice flat names coming from ChatGPT
FLAT_NAMES = [
    "Cozy Studio in Central Paris",
    "Modern Loft Near Eiffel Tower",
    "Charming Flat in Montmartre",
    "Elegant Apartment in Le Marais",
    "Sunny Studio with a View",
    "Beachfront House in Malibu",
    "Penthouse in New York City",
    "Countryside Villa in Tuscany",
    "Skyscraper Suite in Tokyo",
    "Mountain Cabin in Colorado",
    "Riverside Retreat in Bangkok"
]

class Command(BaseCommand):
    help = 'Seed the database with initial flat data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Define the path to the flat images
        path_to_flat_images = os.path.join(settings.BASE_DIR, 'seed_data', 'seed_flats')
        image_files = [f for f in os.listdir(path_to_flat_images) if os.path.isfile(os.path.join(path_to_flat_images, f))]

        # List of sample locations
        paris_locations = [
            {"street": "Rue de Rivoli", "number": "10", "city": "Paris", "country": "France"},
            {"street": "Avenue des Champs-Élysées", "number": "20", "city": "Paris", "country": "France"},
            {"street": "Rue de la Paix", "number": "30", "city": "Paris", "country": "France"},
            {"street": "Boulevard Haussmann", "number": "40", "city": "Paris", "country": "France"},
            {"street": "Rue de Rennes", "number": "50", "city": "Paris", "country": "France"},
        ]
        other_locations = [
            {"street": "Malibu Rd", "number": "100", "city": "Malibu", "country": "USA"},
            {"street": "5th Ave", "number": "200", "city": "New York", "country": "USA"},
            {"street": "Countryside Ln", "number": "300", "city": "Tuscany", "country": "Italy"},
            {"street": "Skyscraper St", "number": "400", "city": "Tokyo", "country": "Japan"},
            {"street": "Mountain Rd", "number": "500", "city": "Colorado", "country": "USA"},
            {"street": "Riverside Dr", "number": "600", "city": "Bangkok", "country": "Thailand"},
        ]

        # Create 11 flats
        for i in range(11):
            if i < 5:
                location = paris_locations[i]
            else:
                location = other_locations[i - 5]
            
            owner = UserProfile.objects.order_by("?").first()  # Randomly assign owner
            name = FLAT_NAMES[i]
            description = fake.text()
            price = random.randrange(30,100,5)

            flat = Flat.objects.create(
                owner=owner,
                street=location["street"],
                number=location["number"],
                city=location["city"],
                country=location["country"],
                name=name,
                description=description,
                price = price
            )

            # Add picture to flat
            if i < len(image_files):
                image_path = os.path.join(path_to_flat_images, image_files[i])
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as f:
                        flat.picture.save(image_files[i], File(f), save=True)
            
            flat.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with 11 flats.'))
