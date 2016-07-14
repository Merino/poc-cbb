from django.views.generic.base import TemplateView


class PatternLayoutBlank(TemplateView):
    template_name = 'pattern_layout_blank.html'

class PatternLayoutList(TemplateView):
    template_name = 'pattern_layout_list.html'

class PatternLayoutRecord(TemplateView):
    template_name = 'pattern_layout_record.html'

class PatternLayoutFocus(TemplateView):
    template_name = 'pattern_layout_focus.html'




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