from django.contrib import admin
from message.models import Message, Client

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body_message')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
