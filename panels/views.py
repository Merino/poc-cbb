

"""

from vesper.views import ModelAdmin
from vesper.forms import Field


"""

from django.contrib import admin

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit




class DemoAdmin(admin.ModelAdmin):


    def get_form(self, request, obj=None, **kwargs):
        form = super(DemoAdmin, self).get_form(request=request, obj=obj, **kwargs)
        form.helper = FormHelper()
        form.helper.layout = Layout(
            'fieldA'
        )

        return form