from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from users.models import Profile, Skill, Message
from django.views import View, generic
from django.contrib.auth.forms import AuthenticationForm
from users.forms import ProfileUserForm, RegisterForm
from users.forms import SkillForm, MessageForm


class ProfilesListView(View):
    def get(self, request):
        profiles = Profile.objects.all()
        context = {'profiles': profiles}
        return render(request, 'profiles/profile.html', context=context)


class UserProfileView(View):
    def get(self, request, pk):
        user_profile = Profile.objects.get(id=pk)
        skills = user_profile.skills.all()
        projects = user_profile.project_set.all()
        context = {
            'profile': user_profile,
            'skills': skills,
            'projects': projects,
        }
        return render(request, 'profiles/user-profile.html', context=context)


class UserAccountView(View):
    def get(self, request):
        profile = request.user.profile
        skills = profile.skills.all()
        projects = profile.project_set.all()
        context = {'profile': profile, 'skills': skills, 'projects': projects}
        return render(request, 'profiles/account.html', context=context)


class UserProfileEditView(View):
    def get(self, request):
        profile = request.user.profile
        profile_form = ProfileUserForm(instance=profile)
        context = {'profile_form': profile_form}
        return render(request, 'profiles/edit-user-profile.html', context=context)

    def post(self, request):
        profile = request.user.profile
        profile_form = ProfileUserForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('account')
        context = {'profile_form': profile_form, 'error': profile_form.errors}
        return render(request, 'profiles/edit-user-profile.html', context=context)


class CreateSkillView(View):
    def get(self, request):
        skill_form = SkillForm()
        context = {'skill_form': skill_form}
        return render(request, 'profiles/skill-form.html', context=context)

    def post(self, request):
        profile = request.user.profile
        skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            skill_form.save(commit=False)
            try:
                skill = Skill.objects.get(name=skill_form.cleaned_data.get('name'))
                profile.skills.add(skill)
                return redirect('account')
            except Skill.DoesNotExist:
                profile.skills.create(name=skill_form.cleaned_data.get('name'),
                                      slug=skill_form.cleaned_data.get('slug'),
                                      description=skill_form.cleaned_data.get('description')
                                      )
            return redirect('account')


class UpdateSkillView(View):
    def get(self, request, skill_slug):
        profile = request.user.profile
        skill = profile.skills.get(slug=skill_slug)
        skill_form = SkillForm(instance=skill)
        context = {'skill_form': skill_form, 'skill_slug': skill_slug}
        return render(request, 'profiles/skill-form.html', context=context)

    def post(self, request, skill_slug):
        profile = request.user.profile
        skill = profile.skills.get(slug=skill_slug)
        skill_form = SkillForm(request.POST, instance=skill)
        if skill_form.is_valid():
            skill_form.save()
            return redirect('account')


class DeleteSkillView(View):
    def get(self, request, skill_slug):
        profile = request.user.profile
        skill = profile.skills.get(slug=skill_slug)
        context = {'deleted_object': skill}
        return render(request, 'profiles/delete.html', context=context)

    def post(self, request, skill_slug):
        profile = request.user.profile
        skill = profile.skills.get(slug=skill_slug)
        profile.skills.remove(skill)
        return redirect('account')


class ProfilesBySkillsView(View):
    def get(self, request, skill_slug):
        skills = get_object_or_404(Skill, slug=skill_slug)
        profiles = Profile.objects.filter(skills__in=[skills])
        context = {
            'profiles': profiles
        }
        return render(request, 'profiles/profile.html', context=context)


class SignUpUser(View):
    def get(self, request):
        register_form = RegisterForm()
        profile_form = ProfileUserForm()
        context = {'register_form': register_form, 'profile_form': profile_form}
        return render(request, 'profiles/signupuser.html', context=context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        profile_form = ProfileUserForm(request.POST, request.FILES)
        if register_form.is_valid() and profile_form.is_valid():
            user = register_form.save()
            profile = Profile.objects.create(
                user=user,
                username=register_form.cleaned_data.get('username'),
                name=profile_form.cleaned_data.get('name'),
                email=profile_form.cleaned_data.get('email'),
                bio=profile_form.cleaned_data.get('bio'),
                intro=profile_form.cleaned_data.get('intro'),
                image=profile_form.cleaned_data.get('image'),
                city=profile_form.cleaned_data.get('city'),
                github=profile_form.cleaned_data.get('github'),
                youtube=profile_form.cleaned_data.get('youtube'),
                twitter=profile_form.cleaned_data.get('twitter'),
                instagram=profile_form.cleaned_data.get('instagram'),
                telegram=profile_form.cleaned_data.get('telegram'),
                linkedin=profile_form.cleaned_data.get('linkedin'),
                website=profile_form.cleaned_data.get('website')
            )
            for skills in profile_form.cleaned_data.get('skills'):
                skill = Skill.objects.get(name=skills)
                profile.skills.add(skill)
            user = authenticate(request, username=register_form.cleaned_data['username'],
                                password=register_form.cleaned_data['password1'])
            login(request, user)
            return redirect('account')
        return redirect('signupuser')


class LoginUserView(View):
    def get(self, request):
        context = {'auth_form': AuthenticationForm()}
        return render(request, 'profiles/loginuser.html', context=context)

    def post(self, request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('account')


class MessageListView(View):
    def get(self, request):
        profile = request.user.profile
        messages = profile.messages.all()
        unread_count = messages.filter(is_read=False).count()
        context = {'messages': messages, 'unread_count': unread_count}
        return render(request, 'profiles/inbox.html', context=context)


class MessageView(View):
    def get(self, request, id):
        profile = request.user.profile
        message = profile.messages.get(id=id)
        if message.is_read == False:
            message.is_read = True
            message.save()
        context = {'message': message, 'id': id}
        return render(request, 'profiles/massage.html', context=context)


class SendMessageView(View):
    def get(self, request, user_id):
        recipient = Profile.objects.get(id=user_id)
        try:
            sender = request.user.profile
        except:
            sender = None
        message_form = MessageForm()
        context = {'recipient': recipient, 'sender': sender, 'message_form': message_form}
        return render(request, 'profiles/message_form.html', context=context)

    def post(self, request, user_id):
        recipient = Profile.objects.get(id=user_id)
        try:
            sender = request.user.profile
        except:
            sender = None
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.sender = sender
            message.recipient = recipient
            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()
            return redirect('user-profile', pk=recipient.id)


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('projects')
