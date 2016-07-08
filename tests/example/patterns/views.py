from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView


class PatternLayoutContentOnly(TemplateView):
    template_name = 'pattern_layout_content_only.html'

class PatternLayoutContentSidebar(TemplateView):
    template_name = 'pattern_layout_content_sidebar.html'

class PatternLogin(TemplateView):
    template_name = 'pattern_login.html'


class PatternDataTable(TemplateView):
    template_name = 'pattern_data_table.html'


class PatternPageHeader(TemplateView):
    template_name = 'pattern_page_header.html'


class PatternError404(TemplateView):
    template_name = 'pattern_error_404.html'


class PatternError500(TemplateView):
    template_name = 'pattern_error_500.html'