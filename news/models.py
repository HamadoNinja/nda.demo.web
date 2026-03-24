from django.db import models
from django.utils.translation import get_language

def pick_lang(ar_value: str, en_value: str) -> str:
    lang = (get_language() or "en").lower()
    if lang.startswith("ar"):
        return ar_value or en_value
    return en_value or ar_value


class News(models.Model):
    title_en = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200, blank=True)

    summary_en = models.TextField(blank=True)
    summary_ar = models.TextField(blank=True)

    content_en = models.TextField(blank=True)   # لو تبي تعتمد على sections خليها blank=True
    content_ar = models.TextField(blank=True)

    image = models.ImageField(upload_to="news/", blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    @property
    def title_i18n(self):
        return pick_lang(self.title_ar, self.title_en)

    @property
    def summary_i18n(self):
        return pick_lang(self.summary_ar, self.summary_en)

    @property
    def content_i18n(self):
        return pick_lang(self.content_ar, self.content_en)

    def __str__(self):
        return self.title_en


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="news/gallery/")

    caption_en = models.CharField(max_length=200, blank=True)
    caption_ar = models.CharField(max_length=200, blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    @property
    def caption_i18n(self):
        return pick_lang(self.caption_ar, self.caption_en)

    def __str__(self):
        return f"{self.news.title_en} - image"


class NewsSection(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="sections")

    title_en = models.CharField(max_length=200, blank=True)
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
        return f"{self.news.title_en} - section"
