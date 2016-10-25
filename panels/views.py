import copy
from django.template import Context
"""

from vesper.views import ModelAdmin
from vesper.forms import Field


"""

from django.contrib import admin
from django.core import urlresolvers
from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .layouts import FormHelper, Layout, TabHolder, Tab, Fieldset, Field



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


class BaseAdmin(TemplateView):
    pass


class EditAdmin(TemplateView):

    def __init__(self, **kwargs):
        super(TemplateView, self).__init__(**kwargs)

        self.model = self.admin.model

    def get(self, request, object_id, *args, **kwargs):
        obj = self.admin.get_object(request=request, object_id=object_id)

        header = self.admin.get_detail_header(request, obj=obj)
        header.subtitle = 'Mail Payment'

        context = {
            'detail_header': header,
            'detail_actions': ['ss']
        }

        return super(EditAdmin, self).get(request, **context)


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

        my_urls = patterns('',
            *extra_urls
        )
        return my_urls + urls

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

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        # Get Object
        obj = self.get_object(request=request, object_id=object_id)

        # Detail Header
        detail_header = self.get_detail_header(request=request, obj=obj)

        # Detail Actions
        info = self.model._meta.app_label, self.model._meta.model_name
        detail_actions = []
        if obj:
            url_delete = urlresolvers.reverse('admin:%s_%s_delete' % info, args=[object_id])
            detail_actions.append(
                Button('delete', 'Delete', url_delete, 'danger', icon='trash')
            )
        url_index = urlresolvers.reverse('admin:%s_%s_changelist' % info)
        detail_actions.append(
            Button('cancel', 'Back', url_index, icon='close')
        )

        detail_actions += copy.copy(self.get_detail_actions(request=request, obj=obj))
        detail_actions.append(
            Button('_continue', 'Save', 'submit', 'primary', icon='save')
        )

        # Render View
        detail_actions_context = []
        for button in detail_actions:
            detail_actions_context.append(
                button.render(
                    None,
                    None,
                    Context({})
                )
            )
        extra_context = {
            'detail_header': detail_header,
            'detail_actions': detail_actions_context,
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