from django.urls import path
from projects.views import ProjectsListView, ProjectDetailView, ProjectsByTagsView, CreateProject, UpdateProject, DeleteProject

urlpatterns = [
    path('', ProjectsListView.as_view(), name='projects'),
    path('project/<str:id>/', ProjectDetailView.as_view(), name='project'),
    path('tag/<str:tag_slug>/', ProjectsByTagsView.as_view(), name='tag'),
    path('create-project/', CreateProject.as_view(), name='create-project'),
    path('update-project/<str:pk>', UpdateProject.as_view(), name='update-project'),
    path('delete-project/<str:pk>', DeleteProject.as_view(), name='delete-project'),

]
