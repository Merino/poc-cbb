from django.contrib import admin
from .models import ListData

class ListDataAdmin(admin.ModelAdmin):
    pass



admin.site.register(ListData, ListDataAdmin)