from django.shortcuts import render, redirect
from .models import Todo  # Import your Todo model

def index(request):
    # Retrieve all Todo objects from the database
    todos = Todo.objects.all()

    if request.method == 'POST':
        # Check if the request is a POST request (e.g., form submission)
        title = request.POST.get('title')
        description = request.POST.get('description')  # Get description from the form

        # Create a new Todo object with title and description and save it to the database
        new_todo = Todo.objects.create(title=title, description=description)

        # Redirect back to the index page
        return redirect('index')

    # Pass the list of todos to the template for rendering
    return render(request, 'index.html', {'todos': todos})

def delete(request, pk):
    # Retrieve the Todo object with the given primary key (pk)
    todo = Todo.objects.get(pk=pk)  # Retrieve the specific Todo item to be deleted based on its primary key (pk)

    # Delete the Todo object
    todo.delete()  # Delete the selected Todo item from the database

    # Redirect back to the index page
    return redirect('index')  # Redirect the user to the index page after deleting a Todo item
