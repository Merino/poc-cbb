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


class SingleInlineView(TemplateView):
    form_class = NestedAForm

    template_name = 'form_inline_single.html'

    inlines = [
        NestedBInline
    ]

    def get_context_data(self, **kwargs):

        formset = self.inlines[0]().get_inline_formsets()

        context = {
            'form': self.form_class(),
            'formset': formset
        }

        return context


    def post(self, request, **kwargs):
        print request
        print kwargs

        formset = self.inlines[0]().get_inline_formsets()(data=request.POST)
        form = self.form_class(data=request.POST)

        if form.is_valid() and formset.is_valid():
            form.save()
            for form in formset:
                form.save()


        context = {
            'form': form,
            'formset': formset
        }

        return self.render_to_response(context)