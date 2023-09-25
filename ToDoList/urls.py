"""ToDoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
    
    Here, we configure the URL patterns for the ToDoList project.
    
    To route URLs to specific views, we use the `path` function, which takes two arguments:
    - The first argument is the URL pattern (as a string).
    - The second argument is the Python function (view) that should handle the request for this URL.

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
    
    This example shows how to associate the root URL ('/') with a function-based view called `home` in the `my_app` app.

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    
    This example demonstrates how to use a class-based view called `Home` in the `other_app` app to handle the root URL ('/').

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
    You can include the URL patterns defined in another URLconf by using the `include` function. This allows you to organize your URL patterns into separate apps and include them here.

"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Define the URL pattern for the admin site
    path('admin/', admin.site.urls),
    
    # Include the URL patterns defined in the 'todo' app's URL configuration
    path('', include('todo.urls'))
]
