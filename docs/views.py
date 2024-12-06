from django.shortcuts import render, get_object_or_404
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'main/index.html', {'projects': projects})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'project_detail.html', {'project': project})
