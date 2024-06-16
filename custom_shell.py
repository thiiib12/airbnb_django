# run this customer shell using >python custome_shell.py



import os
import django
from django.core.management import call_command

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airbnb_django.settings')
django.setup()

# Import your models and other necessary modules
from django.contrib.auth.models import User
from accounts.models import UserProfile
from airbnb.models import Flat
import random
from django.core.files import File

# Optional: Print a welcome message
print("Django environment set up. Models and utilities imported.")

# Start the interactive shell
try:
    # Try to start IPython if available
    from IPython import start_ipython
    start_ipython(argv=[])
except ImportError:
    # Fallback to the standard Python shell
    import code
    code.interact(local=dict(globals(), **locals()))
