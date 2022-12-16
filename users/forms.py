from django import forms
from users.models import Profile, Skill, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input input--text'})
        self.fields['password1'].widget.attrs.update({'class': 'input input--text'})
        self.fields['password2'].widget.attrs.update({'class': 'input input--text'})

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = [
            'Никнейм',
            'Пароль',
            'Подтветждение пароля',

        ]


class ProfileUserForm(forms.ModelForm):
    name = forms.CharField(label='Фамилия Имя', max_length=30, widget=forms.TextInput(attrs={'class': 'input input--text'}))
    email = forms.EmailField(label='E-Mail', max_length=50, widget=forms.EmailInput(attrs={'class': 'input input--email'}))
    bio = forms.CharField(label='О себе', max_length=1000, widget=forms.Textarea(attrs={'class': 'input input--text'}), required=False)
    intro = forms.CharField(label='Основная специальность', max_length=100, widget=forms.TextInput(attrs={'class': 'input input--text'}))
    image = forms.FileField(label='Фотография', required=False)
    city = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'input input--text'}))
    github = forms.CharField(label='GitHub', max_length=100, widget=forms.URLInput(attrs={'class': 'input input--url'}), required=False)
    youtube = forms.CharField(label='YouTube', max_length=100, widget=forms.URLInput(attrs={'class': 'input input--url'}), required=False)
    twitter = forms.CharField(label='Twitter', max_length=100, widget=forms.URLInput(attrs={'class': 'input input--url'}), required=False)
    instagram = forms.CharField(label='Instagram', max_length=100, widget=forms.URLInput(attrs={'class': 'input input--url'}), required=False)
    telegram = forms.CharField(label='Telegram', max_length=100, widget=forms.URLInput(attrs={'class': 'input input--url'}), required=False)
    linkedin = forms.CharField(label='LinkedIn', max_length=100, widget=forms.URLInput(attrs={'class': 'input input--url'}), required=False)
    website = forms.CharField(label='Мой вэб-сайт', max_length=100, widget=forms.URLInput(attrs={'class': 'input input--url'}), required=False)

    class Meta:
        model = Profile
        fields = [
            'name',
            'email',
            'bio',
            'intro',
            'image',
            'city',
            'skills',
            'github',
            'youtube',
            'twitter',
            'instagram',
            'telegram',
            'linkedin',
            'website',

        ]

        widgets = {
            'skills': forms.CheckboxSelectMultiple(),

        }


class SkillForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'input input--text'})
        self.fields['slug'].widget.attrs.update({'class': 'input input--text', 'placeholder': 'Название транслитом прописными символами'})
        self.fields['description'].widget.attrs. update({'class': 'input input--text'})

    class Meta:
        model = Skill
        fields = [
            'name',
            'slug',
            'description',

        ]
        labels = {
            'name': 'Название',
            'slug': 'Слаг',
            'description': 'Описание',

        }


class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'input'})
        self.fields['email'].widget.attrs.update({'class': 'input'})
        self.fields['subject'].widget.attrs.update({'class': 'input'})
        self.fields['body'].widget.attrs.update({'class': 'input'})

    class Meta:
        model = Message
        fields = [
            'name',
            'email',
            'subject',
            'body',

        ]
        labels = {
            'name': 'Фамилия Имя',
            'email': 'E-Mail',
            'subject': 'Тема',
            'body': 'Текст сообщения',

        }



