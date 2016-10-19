from django.template.loader import render_to_string

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, LayoutObject, Field
from crispy_forms.bootstrap import TabHolder, Tab


class Inline(LayoutObject):

    def __init__(self, name, **kwargs):
        self.name = name
        super(LayoutObject, self).__init__(**kwargs)

    def render(self, form, form_style, context, template_pack=None, **kwargs):
        for inline_admin_formset in context['inline_admin_formsets']:
            if self.name == inline_admin_formset.opts.__class__.__name__:
                context['inline_admin_formset'] = inline_admin_formset
                self.template = inline_admin_formset.opts.template
                return render_to_string(self.template, context)