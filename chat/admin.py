# Registers models in Django admin for quick inspection
from django.contrib import admin
from .models import Room, Message

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'author', 'created_at')
    list_filter = ('room', 'created_at')
