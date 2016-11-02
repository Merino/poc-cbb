
from .base import TemplateAdminView
from .forms import FormAdminView, TabularFormAdminInline
from .models import ModelAdminView, TabularModelAdminInline, StackedModelAdminInline

__all__ = [
    'TemplateAdminView',
    'FormAdminView', 'TabularFormAdminInline',
    'ModelAdminView', 'TabularModelAdminInline', 'StackedModelAdminInline'
]