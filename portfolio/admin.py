from django.contrib import admin
from .models import *


class MyProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(MyProject, MyProjectAdmin)
admin.site.register(ProjectImage)
