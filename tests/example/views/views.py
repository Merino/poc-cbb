from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.views.generic.edit import CreateView
from django.views.generic.base import View, TemplateView
# Create your views here.

from .models import NestedA, NestedB


class NestedAForm(ModelForm):
    class Meta:
        model = NestedA


class NestedBForm(ModelForm):
    class Meta:
        model = NestedB


class SingleFormView(CreateView):
    form_class = NestedAForm
    template_name = 'form_single.html'
    success_url = '/views/form/single/'


class BaseInline(object):
    form_class = None

    def get_inline_formsets(self):
        return formset_factory(self.form_class)

class NestedBInline(BaseInline):
    form_class = NestedBForm