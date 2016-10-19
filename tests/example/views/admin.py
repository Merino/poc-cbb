from django.contrib import admin
from .models import ListData


# from vesper.apps import site
# from vesper.views import ModelAdmin
from panels.layouts import Tab, Fieldset, Field
from panels.views import BaseAdmin


class ListDataAdmin(BaseAdmin):

   detail_layout = [
        Tab('General',
            Fieldset('Name',
                Field('name'),
                Field('date'),
            ),
            Fieldset('Status',
                Field('boolean'),
            )
        ),
    ]



admin.site.register(ListData, ListDataAdmin)