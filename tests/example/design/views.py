from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView


class DesignColors(TemplateView):
    template_name = 'design_colors.html'

class DesignGrid(TemplateView):
    template_name = 'design_grid.html'

class DesignIcons(TemplateView):
    template_name = 'design_icons.html'

class DesignIntro(TemplateView):
    template_name = 'design_intro.html'

class DesignLayout(TemplateView):
    template_name = 'design_layout.html'

class DesignMotions(TemplateView):
    template_name = 'design_motions.html'

class DesignTypography(TemplateView):
    template_name = 'design_typography.html'