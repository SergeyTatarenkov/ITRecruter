from projects.models import Project
from django import forms


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'input input--text'})
        self.fields['slug'].widget.attrs.update({'class': 'input input--text'})
        self.fields['image'].widget.attrs.update({'class': 'input input--text'})
        self.fields['description'].widget.attrs.update({'class': 'input input--text'})
        self.fields['tags'].widget.attrs.update({'class': 'input input--checkbox'})
        self.fields['demo_link'].widget.attrs.update({'class': 'input input--url'})
        self.fields['source_link'].widget.attrs.update({'class': 'input input--url'})

    class Meta:
        model = Project
        fields = ['title', 'slug', 'image', 'description', 'tags', 'demo_link', 'source_link']
        labels = {
            'title': 'Название',
            'slug': 'Слаг',
            'image': 'Скриншот проекта',
            'description': 'Описание проекта',
            'tags': 'Тэги',
            'demo_link': 'Ссылка на демо-версию проекта',
            'source_link': 'Ссылка на исходный код на GitHub',

        }
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),

        }
