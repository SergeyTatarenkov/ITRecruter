from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from projects.models import Project, Tag
from projects.forms import ProjectForm


class ProjectsListView(View):
    def get(self, request):
        projects = Project.objects.all()
        context = {'projects': projects}

        return render(request, 'projects/projects.html', context=context)


class ProjectDetailView(View):
    def get(self, request, id):
        project = Project.objects.get(id=id)
        context = {'project': project, 'id': id}
        return render(request, 'projects/single_project.html', context=context)


class CreateProject(View):
    def get(self, request):
        form = ProjectForm()
        context = {'form': form}
        return render(request, 'projects/create-project.html', context=context)

    def post(self, request):
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('projects')


class UpdateProject(View):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        form = ProjectForm(instance=project)
        context = {'form': form}
        return render(request, 'projects/create-project.html', context=context)

    def post(self, request, pk):
        project = Project.objects.get(id=pk)
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')


class DeleteProject(View):
    def get(self, request, pk):
        deleted_project = Project.objects.get(id=pk)
        context = {'deleted_project': deleted_project}
        return render(request, 'projects/delete.html', context=context)

    def post(self, request, pk):
        deleted_project = Project.objects.get(id=pk)
        deleted_project.delete()
        return redirect('projects')


class ProjectsByTagsView(View):
    def get(self, request, tag_slug):
        tag = get_object_or_404(Tag, slug=tag_slug)
        projects = Project.objects.filter(tags__in=[tag])
        context = {'projects': projects}
        return render(request, 'projects/projects.html', context=context)

