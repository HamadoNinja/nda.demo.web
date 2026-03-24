from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from .models import News

from django.utils.translation import gettext as _

@require_GET
def news_list(request):
    qs = News.objects.filter(is_published=True).order_by("-published_at")

    paginator = Paginator(qs, 9)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "news/news_list.html", {
        "page_obj": page_obj,
        "page_title": _("Latest News"),
        "empty_text": _("No news available."),
    })



def news_detail(request, pk):
    news = get_object_or_404(
        News.objects.prefetch_related("sections", "images"),
        pk=pk,
        is_published=True
    )
    return render(request, "news/news_detail.html", {
        "news": news
    })
