from django.shortcuts import render

from projects.models import Project

def home(request):
    featured_projects = Project.objects.filter(
        is_published=True
    ).order_by('-created_at')[:3]  # آخر 3 مشاريع

    return render(request, "home/home.html", {
        "featured_projects": featured_projects
    })


