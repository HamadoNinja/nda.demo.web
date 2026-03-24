# projects/models.py
from django.db import models
from django.utils.translation import get_language


def pick_lang(ar_value: str, en_value: str) -> str:
    lang = (get_language() or "en").lower()
    if lang.startswith("ar"):
        return ar_value or en_value
    return en_value or ar_value


class Project(models.Model):
    title_en = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200, blank=True)

    summary_en = models.TextField(blank=True)
    summary_ar = models.TextField(blank=True)

    description_en = models.TextField()
    description_ar = models.TextField(blank=True)

    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    @property
    def title_i18n(self):
        return pick_lang(self.title_ar, self.title_en)

    @property
    def summary_i18n(self):
        return pick_lang(self.summary_ar, self.summary_en)

    @property
    def description_i18n(self):
        return pick_lang(self.description_ar, self.description_en)

    def __str__(self):
        return self.title_en


class ProjectSection(models.Model):
    project = models.ForeignKey(
        Project, related_name="sections", on_delete=models.CASCADE
    )

    title_en = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200, blank=True)

    body_en = models.TextField()
    body_ar = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    @property
    def title_i18n(self):
        return pick_lang(self.title_ar, self.title_en)

    @property
    def body_i18n(self):
        return pick_lang(self.body_ar, self.body_en)

    def __str__(self):
        return self.title_en


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to="projects/gallery/")

    caption_en = models.CharField(max_length=255, blank=True)
    caption_ar = models.CharField(max_length=255, blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    @property
    def caption_i18n(self):
        return pick_lang(self.caption_ar, self.caption_en)

    def __str__(self):
        return f"{self.project.title_en} - image"
