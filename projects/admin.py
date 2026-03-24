from django.contrib import admin
from django.utils.translation import get_language
from .models import Project, ProjectSection, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectSectionInline(admin.TabularInline):
    model = ProjectSection
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title_current", "is_published", "created_at")
    list_filter = ("is_published",)
    search_fields = ("title_en", "title_ar", "summary_en", "summary_ar", "description_en", "description_ar")
    inlines = [ProjectSectionInline, ProjectImageInline]

    @admin.display(description="Title")
    def title_current(self, obj):
        lang = get_language() or "en"
        if lang.startswith("ar"):
            return obj.title_ar or obj.title_en
        return obj.title_en or obj.title_ar
