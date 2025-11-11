from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                         # Home with room/user form
    path('room/<str:name>/', views.room, name='room'),         # Room page
    path('checkview', views.checkview, name='checkview'),      # POST target from home.html
    path('getMessages/<str:room>/', views.get_messages, name='get_messages'),  # AJAX poll
    path('send', views.send, name='send'),                     # AJAX send
]
