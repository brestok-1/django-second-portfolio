from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class MyProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'description')
    list_display_links = ('title',)
    search_fields = ('descrtiption', 'issues', 'solve')
    prepopulated_fields = {'slug': ('title',)}


class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'get_html_photo')
    list_display_links = ('project',)

    def get_html_photo(self, object):  # object refers to an object of the women class
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width=50 height = 50>')

    get_html_photo.short_description = 'Image'


admin.site.register(MyProject, MyProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
