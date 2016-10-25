# Create your views here.
from django.views.generic.base import TemplateView


class FoundationColors(TemplateView):
    template_name = 'foundation_colors.html'

class FoundationGrid(TemplateView):
    template_name = 'foundation_grid.html'

# needs to go to panels
# class FoundationBlocks(TemplateView):
#     template_name = 'design_blocks.html'

class FoundationIcons(TemplateView):
    template_name = 'foundation_icons.html'

class FoundationIndex(TemplateView):
    template_name = 'foundation_index.html'

class FoundationLayout(TemplateView):
    template_name = 'foundation_layout.html'

class FoundationMotions(TemplateView):
    template_name = 'foundation_motions.html'

class FoundationTypography(TemplateView):
    template_name = 'foundation_typography.html'

class FoundationNavigation(TemplateView):
    template_name = 'foundation_navigation.html'

class FoundationVoiceAndTone(TemplateView):
    template_name =  'foundation_voice_and_tone.html'