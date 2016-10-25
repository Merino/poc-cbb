import copy
from django.template import Context
"""

from vesper.views import ModelAdmin
from vesper.forms import Field


"""

from django.contrib import admin
from django.core import urlresolvers

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



class BaseAdmin(nested_admin.NestedModelAdmin):

    # List View
    list_fields = []
    list_filters = []
    list_actions = []
    list_search = []

    # Detail View
    detail_layout = []
    detail_actions = []

    # Templates
    change_form_template = 'vds_object_edit.html'

    # def __init__(self, *args, **kwargs):
    #     #self.detail_actions = []
    #     #self.detail_layout = []
    #
    #     super(BaseAdmin, self).__init__(*args, **kwargs)

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
        form = super(BaseAdmin, self).get_form(request, obj, **kwargs)

        form.helper = FormHelper()
        form.helper.form_tag = False
        form.helper.layout = self.get_form_layout(request, obj, **kwargs)
        form.helper.template_pack = 'vds/forms'

        return form

    def get_detail_header(self, request, obj=None, **kwargs):
        """
        """
        detail_header = {
            'title': 'JUB',
            'subtitle': False,
            'icon': 'True'
        }

        return detail_header

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
        detail_actions += copy.copy(self.get_detail_actions(request=request, obj=obj))
        url_index = urlresolvers.reverse('admin:%s_%s_changelist' % info)
        detail_actions.append(
            Button('cancel', 'Back', url_index, icon='close')
        )
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

        response = super(BaseAdmin, self).changeform_view(
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