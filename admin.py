from django.contrib import admin
from leeps_website.projects.models import Project, Grant

class ProjectAdmin(admin.ModelAdmin):
    pass

class GrantAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Grant, GrantAdmin)

from leeps_website.fire.models import Kindling, Configuration

class KindlingAdmin(admin.ModelAdmin):
    pass

class ConfigurationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Kindling, KindlingAdmin)
admin.site.register(Configuration, ConfigurationAdmin)
    
from leeps_website.papers.models import Paper

class PaperAdmin(admin.ModelAdmin):
    pass

admin.site.register(Paper, PaperAdmin)

from leeps_website.people.models import Person, Category

class PersonAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)
admin.site.register(Category, CategoryAdmin)

from leeps_website.classes.models import Class, Reading

class ClassAdmin(admin.ModelAdmin):
    pass

class ReadingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Class, ClassAdmin)
admin.site.register(Reading, ReadingAdmin)
