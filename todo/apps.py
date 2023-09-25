from django.apps import AppConfig

# Define a custom configuration class for the 'todo' app.
class TodoConfig(AppConfig):
    # Specify the name of the app, which should match the name of the app folder.
    # In this case, 'name' should be 'todo' since your app is named 'todo'.
    name = 'todo'

# The AppConfig class is used to configure an app and provides metadata about the app.
# In this case, it's being used to configure the 'todo' app.
