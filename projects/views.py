# projects/views.py
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from .models import Project

def projects_list(request):
    projects = Project.objects.filter(is_published=True).order_by("-created_at")
    return render(request, "projects/projects_list.html", {
        "projects": projects,
        "page_title": _("Our Projects"),
        "empty_text": _("No projects available."),
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, is_published=True)
    return render(request, "projects/project_detail.html", {
        "project": project
    })
