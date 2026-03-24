from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "created_at", "email_sent")
    search_fields = ("name", "phone", "email", "message")
    list_filter = ("email_sent", "created_at")
