from itertools import chain

from django.forms.widgets import Textarea, Input, Select, RadioSelect, RadioChoiceInput
from django.forms.utils import flatatt
from django.template.loader import render_to_string


class InputWidget(Input):
    """
    """
    def __init__(self, attrs=None):
        super(InputWidget, self).__init__(attrs)
        self.attrs.update({
            'class': 'vds-input'
        })


class RadioSelectWidget(RadioSelect):
    """
    """
    template_name = 'vds/forms/widgets/radioselect.html'

    def render(self, name, value, attrs=None, choices=()):
        choices = []
        index = 0

        for choice in list(chain(self.choices, choices)):
            widget = RadioChoiceInput(name=name, value=value, attrs=attrs.copy(), choice=choice, index=index)
            choices.append(widget)
            index = index + 1

        context = {
            'name': name,
            'choices': choices
        }

        return render_to_string(self.template_name, context=context)


class ForeignKeyWidget(Select):
    """
    """
    template_name = 'vds/forms/widgets/foreignkey.html'

    def render(self, name, value, attrs=None):

        attrs.update({
            'class':'vds-select'
        })

        html = super(ForeignKeyWidget, self).render(name, value, attrs)

        return html


class RichTextareaWidget(Textarea):
    """
    """
    template_name = 'vds/forms/widgets/richtextarea.html'

    class Media:
        js = (
                '/static/vesper/libs/tinymce/tinymce.min.js',
        )

    def render(self, name, value, attrs=None):
        attrs = self.build_attrs(attrs, name=name)

        context = {
            'attrs': flatatt(attrs),
            'name': name,
            'value': value,
            'id': attrs['id']
        }

        return render_to_string(self.template_name, context=context)


class HtmlWidget(Textarea):
    """
    """
    pass