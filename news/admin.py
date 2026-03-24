from django.contrib import admin
from .models import News, NewsImage, NewsSection


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1


class NewsSectionInline(admin.TabularInline):
    model = NewsSection
    extra = 1


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title_current", "is_published", "published_at")
    list_filter = ("is_published",)
    search_fields = (
        "title_en", "title_ar",
        "summary_en", "summary_ar",
        "content_en", "content_ar",
    )
    inlines = [NewsSectionInline, NewsImageInline]

    @admin.display(description="Title")
    def title_current(self, obj):
        return obj.title_i18n
