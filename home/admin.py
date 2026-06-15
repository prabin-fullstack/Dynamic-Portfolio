from django.contrib import admin
from .models import SkillCategory,Technology,Project,Contact
# Register your models here.

admin.site.register(SkillCategory)
admin.site.register(Technology)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('technologies',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'subject',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
    )