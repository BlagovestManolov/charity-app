from django.contrib import admin

from charity_app.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('organization_id', 'project_name', 'project_type', 'is_active', 'date_of_creation')
    list_filter = ('project_type', 'date_of_creation')
    ordering = ('organization_id',)
