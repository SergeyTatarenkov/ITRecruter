from django.contrib import admin
from users.models import Skill, Profile


class SkillAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'description',

    ]


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'username',
        'intro',
        'email',

    ]
    list_filter = [
        'skills',
        'intro',

    ]
    search_fields = [
        'name',
        'username',
        'skills',
        'bio',
        'intro',

    ]


admin.site.register(Skill, SkillAdmin)
admin.site.register(Profile, ProfileAdmin)
