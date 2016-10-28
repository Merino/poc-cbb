import copy
from django.template import Context
"""

from vesper.views import ModelAdmin
from vesper.forms import Field


"""

from django.contrib import admin
from django.core import urlresolvers
from django.conf.urls import url
from django.db import models
from django.forms import formset_factory
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .layouts import FormHelper, Layout, TabHolder, Tab, Fieldset, Field
from .widgets import ForeignKeyWidget, InputWidget


import nested_admin

#from .models import Product, Category, CategoryItem, Author, Genre, Book, Chapter, Section

# from vesper.apps import site
# from vesper.views import ModelAdmin
# from vesper.layouts import Tab, FieldSet, Field

# Register your models here.
from .layouts import Button

# class CategoryAdmin(nested_admin.NestedModelAdmin):
#     pass
#
#
# class CategoryItemAdminInline(nested_admin.NestedStackedInline):
#     model = CategoryItem
#     extra = 0


# class HeaderAdminMixin(object):
#     """
#     """
#
#     page_title = None
#
#     header_title = None
#     header_subtitle = None
#     header_icon = None
#     header_icon_color = None
#
#     header_actions = []
#
#     def get_header(self, request, obj=None, actions=[], **kwargs):
#         pass
#
#     def _render_header(self, render):
#
#         context = {}
#
#         return context
#



class TabularInlineAdmin(nested_admin.NestedTabularInline):
    extra = 0

    template = 'vds_inline_tabular.html'

    formfield_overrides = {
        models.ForeignKey: {'widget': ForeignKeyWidget},
        models.CharField: {'widget': InputWidget},
    }

class StackedInlineAdmin(nested_admin.NestedStackedInline):
    template = 'vds_inline_stacked.html'

    extra = 0

    formfield_overrides = {
        models.ForeignKey: {'widget': ForeignKeyWidget},
        models.CharField: {'widget': InputWidget},
    }



class BaseAdmin(TemplateView):
    """
    """
    pass


class EditAdmin(FormView):
    """
    """

    inlines = []

    def __init__(self, **kwargs):
        super(EditAdmin, self).__init__(**kwargs)
        self.model = self.admin.model

    def get_form_layout(self):
        """
        """
        return self.form_layout

    def get_form(self, form_class=None):
        """
        Returns an instance of the form to be used in this view.
        """
        if form_class is None:
            form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())

        #form = super(EditAdmin, self).get_form()

        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = self.get_form_layout()
        form.helper.template_pack = 'vds/forms'

        return form

    def get_success_url(self):
        return self.admin.get_url_reverse('change', self.object.pk)

    def get_object(self, request, object_id):
        """
        """
        return self.admin.get_object(request=request, object_id=object_id)

    def get_context_data(self, request=None, **kwargs):

        header = self.admin.get_detail_header(request, obj=self.object)
        header.subtitle = 'Mail Payment'

        buttons = [
            Button(name='submit', value='Submit', link='submit', style='primary'),
            Button(name='submit', value='Submit', link='submit', style='brand'),
        ]

        context = {
            'detail_header': header,
            'detail_actions': self._render_buttons(buttons),
            'object': self.object
        }

        kwargs.update(context)

        context = super(EditAdmin, self).get_context_data(**kwargs)

        formsets = []

        if self.inlines:
            for inline in self.inlines:
                formset = formset_factory(inline, extra=0)
                formsets.append(formset())

        context.update({
            'formsets':formsets
        })

        return context

    def get(self, request, object_id, *args, **kwargs):
        """
        """
        self.object = self.get_object(request=request, object_id=object_id)



        context = self.get_context_data(request=request)

        print context

        return self.render_to_response(context)

        #return super(EditAdmin, self).get(request, **context)

    def post(self, request, object_id, *args, **kwargs):
        """
        """
        self.object = self.get_object(request=request, object_id=object_id)

        kwargs = self.get_context_data(request=request)

        return super(EditAdmin, self).post(request, *args, **kwargs)


    def _render_buttons(self, buttons):
        render_buttons = []
        for button in buttons:
            render_buttons.append(
                button.render(
                    None,
                    None,
                    Context({})
                )
            )

        return render_buttons


class ModelAdmin(nested_admin.NestedModelAdmin):

    # List View
    list_fields = []
    list_filters = []
    list_actions = []
    list_search = []

    # Detail View
    detail_layout = []
    detail_actions = []

    # Extra Views
    views = []

    # Templates
    change_form_template = 'vds_object_edit.html'

    formfield_overrides = {
        models.ForeignKey: {'widget': ForeignKeyWidget},
    }

    #   Views Functions
    # ---------------------
    def get_urls(self):
        urls = super(ModelAdmin, self).get_urls()
        extra_urls = []
        for view in self.views:
            name = '%s_%s_%s' % (self.model._meta.app_label, self.model._meta.model_name, view.name)

            extra_urls.append(
                url(view._regex, view._callback.as_view(admin=self), name=name)
            )

        return extra_urls + urls

    def get_url_reverse(self, name, *args):
        info = self.model._meta.app_label, self.model._meta.model_name, name
        return urlresolvers.reverse('admin:%s_%s_%s' % info, args=args)

    #   List Functions
    # ---------------------

    #   Detail Functions
    # ---------------------
    def get_form_layout(self, request, obj=None, **kwargs):
        """
        """
        layout = Layout(
            TabHolder(
                *self.detail_layout
            )
        )
        return layout

    def get_form(self, request, obj=None, **kwargs):
        """
        """
        form = super(ModelAdmin, self).get_form(request, obj, **kwargs)

        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = self.get_form_layout(request, obj, **kwargs)
        form.helper.template_pack = 'vds/forms'

        return form

    def get_detail_header(self, request, obj=None, **kwargs):
        """
        """
        class Header(object):
            title = None
            subtitle = None
            icon = None

        header = Header()

        if obj:
            header.title = obj
        else:
            header.title = 'Add %s' % self.model._meta

        header.subtitle = False
        header.icon = "flag"

        return header

    def get_detail_actions(self, request, obj=None, **kwargs):
        """
        """
        return self.detail_actions

    def _render_buttons(self, buttons):
        render_buttons = []
        for button in buttons:
            render_buttons.append(
                button.render(
                    None,
                    None,
                    Context({})
                )
            )

        return render_buttons


    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        # Get Object
        obj = self.get_object(request=request, object_id=object_id)

        # Detail Header
        detail_header = self.get_detail_header(request=request, obj=obj)

        # Detail Actions
        detail_actions = []
        if obj:
            url_delete = self.get_url_reverse('delete', obj.pk)
            detail_actions.append(
                Button('delete', 'Delete', url_delete, 'danger', icon='trash')
            )
        url_index = self.get_url_reverse('changelist')
        detail_actions.append(
            Button('cancel', 'Back', url_index, icon='close')
        )

        detail_actions += copy.copy(self.get_detail_actions(request=request, obj=obj))
        detail_actions.append(
            Button('_continue', 'Save', 'submit', 'primary', icon='save')
        )

        # Render View
        extra_context = {
            'detail_header': detail_header,
            'detail_actions': self._render_buttons(buttons=detail_actions),
        }

        response = super(ModelAdmin, self).changeform_view(
                                                request=request,
                                                object_id=object_id,
                                                form_url='',
                                                extra_context=extra_context
                                            )
        return response


# class ProductAdmin(BaseAdmin):
#
#
#       inlines = [
#         CategoryItemAdminInline
#    ]
#     detail_layout = [
#         Tab('General',
#             Fieldset('Name',
#                 Field('sku'),
#                 Field('name'),
#             ),
#             Fieldset('Status',
#                 Field('active'),
#             )
#         ),
#         Tab('Collection',
#             Inline('CategoryItemAdminInline'),
#         ),
#         Tab('Brand',
#             Field('brand'),
#             Field('brand_mpn'),
#         ),
#     ]
#
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)
#
#
# class SectionAdminInline(nested_admin.NestedTabularInline):
#     model = Section
#     extra = 0
#
#
# class ChapterAdminInline(nested_admin.NestedTabularInline):
#     model = Chapter
#     extra = 0
#
#     inlines = [
#         SectionAdminInline
#     ]
#
#
#
#
#
# class AuthorAdmin(nested_admin.NestedModelAdmin):
#     pass
#
# class GenreAdmin(nested_admin.NestedModelAdmin):
#     pass
#
#
# class BookAdmin(BaseAdmin):
#
#     inlines = [
#         ChapterAdminInline,
#     ]
#
#     detail_layout = [
#         Tab('General',
#             Fieldset('Name',
#                 Field('title'),
#
#             ),
#             Fieldset('Author',
#                 Field('genre'),
#                 Field('author'),
#             )
#         ),
#         Tab('Chapters',
#             Inline('ChapterAdminInline'),
#         ),
#     ]
#
#
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Genre, GenreAdmin)
# admin.site.register(Book, BookAdmin)