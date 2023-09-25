
from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        # Create a new Todo object with title and description and save it to the database
        new_todo = Todo.objects.create(title=title, description=description)
        
        # Redirect back to the index page
        return redirect('index')

    return render(request, 'index.html', {'todos': todos})

def update(request, pk):
    # Retrieve the Todo object to be updated
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        # Handle the form submission to update the Todo item
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Update the Todo item with the new data
        todo.title = title
        todo.description = description
        todo.save()

        # Redirect back to the index page
        return redirect('index')

    # Render a template for updating the Todo item
    return render(request, 'index.html', {'todo': todo})  # Reuse the same 'index.html' template

def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('index')