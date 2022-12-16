from django.contrib import admin

from projects.models import Project, Tag, Review


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    list_filter = ['name', ]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['value', 'review_text', 'created_at']
    list_filter = ['value', ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Review, ReviewAdmin)

