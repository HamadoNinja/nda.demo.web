from django.shortcuts import render, get_object_or_404
from .models import Video

def video_list(request):
    videos = Video.objects.filter(is_published=True)
    return render(request, "videos/video_list.html", {
        "videos": videos
    })

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk, is_published=True)
    return render(request, "videos/video_detail.html", {
        "video": video
    })
