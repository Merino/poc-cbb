from django.contrib import admin
from .models import ListData


# from vesper.apps import site
# from vesper.views import ModelAdmin
# from vesper.layouts import Tab, FieldSet, Field


class ListDataAdmin(admin.ModelAdmin):
    pass



admin.site.register(ListData, ListDataAdmin)