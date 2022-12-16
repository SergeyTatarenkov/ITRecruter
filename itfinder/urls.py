"""itfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users.views import ProfilesListView, UserProfileView, ProfilesBySkillsView, SignUpUser, \
    logoutuser, LoginUserView, UserAccountView, UserProfileEditView, CreateSkillView, UpdateSkillView, DeleteSkillView, MessageListView, MessageView, SendMessageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('users/', ProfilesListView.as_view(), name='users'),
    path('users/<str:pk>', UserProfileView.as_view(), name='user-profile'),
    path('skills/<str:skill_slug>', ProfilesBySkillsView.as_view(), name='skills'),
    path('signupuser/', SignUpUser.as_view(), name='signupuser'),
    path('logoutuser', login_required(logoutuser), name='logoutuser'),
    path('loginuser/', LoginUserView.as_view(), name='loginuser'),
    path('account/', login_required(UserAccountView.as_view(), login_url='/loginuser'), name='account'),
    path('edit-user-profile/', login_required(UserProfileEditView.as_view(), login_url='/loginuser'), name='edit-user-profile'),
    path('create-skill/', login_required(CreateSkillView.as_view(), login_url='/loginuser'), name='create-skill'),
    path('update-skill/<slug:skill_slug>', login_required(UpdateSkillView.as_view(), login_url='/loginuser'), name='update-skill'),
    path('delete-skill/<slug:skill_slug>', login_required(DeleteSkillView.as_view(), login_url='/loginuser'), name='delete-skill'),
    path('inbox/', login_required(MessageListView.as_view(), login_url='/loginuser'), name='inbox'),
    path('message/<str:id>', login_required(MessageView.as_view(), login_url='/loginuser'), name='message'),
    path('send_message/<str:user_id>', SendMessageView.as_view(), name='send-message'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
