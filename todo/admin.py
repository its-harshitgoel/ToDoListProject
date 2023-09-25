# Import the necessary module to work with the Django admin interface.
from django.contrib import admin

# Import the Todo model from the current application's models.py file.
from .models import Todo

# Register the Todo model with the Django admin site.
# This allows you to manage (CRUD operations) Todo objects via the admin interface.
admin.site.register(Todo)
