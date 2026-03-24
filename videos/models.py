from django.db import models
from django.utils.translation import get_language
import re


def pick_lang(ar, en):
    lang = (get_language() or "en").lower()
    if lang.startswith("ar"):
        return ar or en
    return en or ar


class Video(models.Model):
    title_en = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200, blank=True)

    description_en = models.TextField(blank=True)
    description_ar = models.TextField(blank=True)

    youtube_url = models.URLField()

    thumbnail = models.ImageField(
        upload_to="videos/thumbs/",
        blank=True,
        null=True
    )

    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_at"]

    @property
    def title_i18n(self):
        return pick_lang(self.title_ar, self.title_en)

    @property
    def description_i18n(self):
        return pick_lang(self.description_ar, self.description_en)

    @property
    def youtube_embed_url(self):
        url = self.youtube_url or ""

        patterns = [
            r"youtu\.be/([^?&/]+)",
            r"youtube\.com/watch\?v=([^?&/]+)",
            r"youtube\.com/embed/([^?&/]+)",
            r"youtube\.com/shorts/([^?&/]+)",
        ]

        video_id = None
        for p in patterns:
            match = re.search(p, url)
            if match:
                video_id = match.group(1)
                break

        if not video_id:
            return ""

        return f"https://www.youtube.com/embed/{video_id}"

    def __str__(self):
        return self.title_en
