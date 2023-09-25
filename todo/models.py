from django.db import models

class Todo(models.Model):
    # Define a field for the title of the todo item with a maximum length of 200 characters
    title = models.CharField(max_length=200)

    # Define a field for the description of the todo item as a text field with a default value of an empty string
    description = models.TextField(default='')

    def __str__(self):
        # This method returns a human-readable string representation of the todo item,
        # which is the title of the todo item.
        return self.title
