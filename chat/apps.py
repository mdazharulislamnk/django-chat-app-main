# App configuration for the chat app
from django.apps import AppConfig

class ChatConfig(AppConfig):
    name = 'chat'
    default_auto_field = 'django.db.models.BigAutoField'  # consistent PKs
