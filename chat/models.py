# Data models for rooms and messages
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)  # room identifier

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')  # room link
    author = models.CharField(max_length=50)  # simple username field (no auth integration)
    content = models.TextField()              # message text
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp

    def __str__(self):
        return f'{self.author}: {self.content[:20]}'
