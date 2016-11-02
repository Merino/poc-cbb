from __future__ import unicode_literals

from django.template import Template
from django.template.loader import render_to_string
from django.utils.html import conditional_escape

from crispy_forms.compatibility import text_type
from crispy_forms.utils import flatatt

from crispy_forms.helper import FormHelper
from crispy_forms.layout import LayoutObject, Layout, Field, Button
from crispy_forms.bootstrap import ContainerHolder, Container


TEMPLATE_PACK = 'vds/forms'


class TabHolder(ContainerHolder):
    """
    TabHolder object. It wraps Tab objects in a container. Requires bootstrap-tab.js::

        TabHolder(
            Tab('form_field_1', 'form_field_2'),
            Tab('form_field_3')
        )
    """
    template = '%s/layout/tab.html'

    def render(self, form, form_style, context, template_pack=None, **kwargs):
        for tab in self.fields:
            tab.active = False

        # Open the group that should be open.
        self.open_target_group_for_form(form)
        content = self.get_rendered_fields(form, form_style, context, template_pack)
        links = ''.join(tab.render_link(form, template_pack) for tab in self.fields)

        context.update({
            'tabs': self,
            'links': links,
            'content': content
        })
        template = self.get_template_name(template_pack)
        return render_to_string(template, context.flatten())


class Tab(Container):
    """
    Tab object. It wraps fields in a div whose default class is "tab-pane" and
    takes a name as first argument. Example::

        Tab('tab_name', 'form_field_1', 'form_field_2', 'form_field_3')
    """
    css_class = 'vds-tabs--default__content'
    link_template = '%s/layout/tab-link.html'

    errors = True

    def _has_errors(self, form):
        for field in self.fields:
            if field.errors:
                return True
        else:
            return False

    def render_link(self, form, template_pack=TEMPLATE_PACK, **kwargs):
        """
        Render the link for the tab-pane. It must be called after render so css_class is updated
        with active if needed.
        """

        self.errors = self._has_errors(form=form)

        link_template = self.link_template % template_pack
        return render_to_string(link_template, {'link': self})

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        if self.active:
            self.css_class = 'vds-tabs--default__content vds-show'
        else:
            self.css_class = 'vds-tabs--default__content vds-hide'

        return super(Container, self).render(form, form_style, context, template_pack)


class Fieldset(LayoutObject):
    """
    Layout object. It wraps fields in a <fieldset>

    Example::

        Fieldset("Text for the legend",
            'form_field_1',
            'form_field_2'
        )

    The first parameter is the text for the fieldset legend. This text is context aware,
    so you can do things like::

        Fieldset("Data for {{ user.username }}",
            'form_field_1',
            'form_field_2'
        )
    """
    template = "%s/layout/fieldset.html"

    def _has_errors(self, form):
        for field in self.fields:
            if field.errors:
                return True
        else:
            return False

    def __init__(self, legend, *fields, **kwargs):
        self.fields = list(fields)
        self.legend = legend
        self.css_class = kwargs.pop('css_class', '')
        self.css_id = kwargs.pop('css_id', None)
        self.template = kwargs.pop('template', self.template)
        self.flat_attrs = flatatt(kwargs)
        self.errors = False

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        fields = self.get_rendered_fields(form, form_style, context, template_pack, **kwargs)

        self.errors = self._has_errors(form=form)

        legend = ''
        if self.legend:
            legend = '%s' % Template(text_type(self.legend)).render(context)

        template = self.get_template_name(template_pack)
        return render_to_string(
            template,
            {'fieldset': self, 'legend': legend, 'fields': fields, 'form_style': form_style}
        )


class Field(LayoutObject):
    """
    Layout object, It contains one field name, and you can add attributes to it easily.
    For setting class attributes, you need to use `css_class`, as `class` is a Python keyword.

    Example::

        Field('field_name', style="color: #333;", css_class="whatever", id="field_name")
    """
    template = "%s/layout/field.html"

    def __init__(self, *args, **kwargs):
        self.fields = list(args)
        self.attrs = {}

        if not hasattr(self, 'attrs'):
            self.attrs = {}

        if 'css_class' in kwargs:
            if 'class' in self.attrs:
                self.attrs['class'] += " %s" % kwargs.pop('css_class')
            else:
                self.attrs['class'] = kwargs.pop('css_class')

        self.wrapper_class = kwargs.pop('wrapper_class', None)
        self.template = kwargs.pop('template', self.template)

        # We use kwargs as HTML attributes, turning data_id='test' into data-id='test'
        self.attrs.update(dict([(k.replace('_', '-'), conditional_escape(v)) for k, v in kwargs.items()]))
        self.errors = False

    def _has_errors(self, form):
        if self.fields[0] in form.errors.keys():
            return True
        else:
            return False

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, extra_context=None, **kwargs):
        if extra_context is None:
            extra_context = {}
        if hasattr(self, 'wrapper_class'):
            extra_context['wrapper_class'] = self.wrapper_class

        template = self.get_template_name(template_pack)

        self.errors = self._has_errors(form=form)


        field_class =  form.fields.get(self.fields[0])

        if 'choices' in field_class.widget.__dict__:
            self.attrs['class'] = 'vds-select'
        else:
            self.attrs['class'] = 'vds-input'


        return self.get_rendered_fields(
            form, form_style, context, template_pack,
            template=template, attrs=self.attrs, extra_context=extra_context,
            **kwargs
        )


class Inline(LayoutObject):
    """
    """

    def __init__(self, name, **kwargs):
        self.fields = list()
        self.name = name
        self.errors = False
        super(LayoutObject, self).__init__(**kwargs)

    def render(self, form, form_style, context, template_pack=None, **kwargs):

        try:
            for inline_admin_formset in context['inline_admin_formsets']:
                if self.name == inline_admin_formset.opts.__class__.__name__:
                    context['inline_admin_formset'] = inline_admin_formset
                    self.template = inline_admin_formset.opts.template
                    return render_to_string(self.template, context)
        except:
            for inline_formset in context['inline_formsets']:
                if self.name == inline_formset.name:
                    formset = inline_formset.get_formset()
                    context['inline_formset'] = formset
                    self.template = 'vds/forms/inlines/base.html'
                    return render_to_string(self.template, context)


class Button(Button):
    """
        Button("id", "name", "type")
        Button("id-cnl", "Cancel", "/sss/")

        Button('id-save', _("Save"), "submit", "primary")
        Button('id-cancel', _("Cancel"), "/action/delete", style="primary")

        Button('id-cancel', _("Cancel"), "/action/delete", style="danger", icon="danger")
    """
    template = '%s/layout/button.html'
    input_type = 'button'

    def __init__(self, name, value, link, style='secondary', *args, **kwargs):

        super(Button, self).__init__(name=name, value=value, *args, **kwargs)

        # Link
        if link == 'submit':
            self.input_type = 'submit'
        else:
            self.input_type = 'a'
            self.attrs = {
                'href': link
            }

        # Style
        self.field_classes = 'vds-button'
        if style == 'secondary':
            self.field_classes += ' vds-button--neutral'

        if style == 'primary':
            self.field_classes += ' vds-button--brand'

        if style == 'danger':
            self.field_classes += ' vds-button--destructive'

        # Icon
        try:
            self.icon = kwargs['icon']
        except:
            self.icon = False

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        """
        Renders an `<button />` if container is used as a Layout object.
        Input button value can be a variable in context.
        """
        self.value = Template(text_type(self.value)).render(context)
        template = self.get_template_name(template_pack)

        self.attrs.update({
            'class': self.field_classes,
            'value': self.value,
            'name': self.name,
        })

        self.flat_attrs = flatatt(self.attrs)

        return render_to_string(template, {'button': self}, context)