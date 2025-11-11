# Routes the root of the site into the chat app
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),     # Django admin
    path('', include('chat.urls')),      # chat app handles the site
]
