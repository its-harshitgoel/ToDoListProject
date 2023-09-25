from django.shortcuts import render, redirect
from django.urls import path
from . import views

# Define the URL patterns for your Django application
urlpatterns = [
    # This URL pattern matches the root URL (e.g., http://127.0.0.1:8000/)
    # and associates it with the 'index' view function from the 'views' module.
    # The name 'index' is used as an identifier for this URL pattern.
    path('', views.index, name='index'),

    # This URL pattern uses angle brackets '<>' to capture an integer value
    # as a variable named 'pk' from the URL (e.g., /delete/1/).
    # It associates this URL pattern with the 'delete' view function from the 'views' module.
    # The 'name' attribute is set to 'delete' for identification.
    path('delete/<int:pk>/', views.delete, name='delete'),

    path('update/<int:pk>/', views.update, name='update')

]
