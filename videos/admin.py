from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title_en", "title_ar", "is_published", "published_at")
    list_filter = ("is_published",)
    search_fields = (
        "title_en", "title_ar",
        "description_en", "description_ar"
    )
