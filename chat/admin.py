from django.contrib import admin
from .models import User, Chat


class UserAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('id', 'username', 'tokens')
    search_fields = ('username',)  # Enable search functionality by username
    list_filter = ('tokens',)  # Add filter options for tokens
    ordering = ('-tokens',)  # Sort users by tokens in descending order
    readonly_fields = ('id',)  # Make the ID field read-only


class ChatAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('id', 'user', 'message', 'response', 'timestamp')
    # Enable search functionality
    search_fields = ('message', 'response', 'user__username')
    list_filter = ('timestamp',)  # Add filter options for timestamps
    ordering = ('-timestamp',)  # Sort chats by most recent first
    # Make the ID and timestamp fields read-only
    readonly_fields = ('id', 'timestamp')


# Register the models with the admin site
admin.site.register(User, UserAdmin)
admin.site.register(Chat, ChatAdmin)
