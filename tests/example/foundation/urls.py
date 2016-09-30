from django.conf.urls import url

from .views import FoundationIndex, FoundationColors, FoundationGrid, FoundationIcons, FoundationLayout, FoundationMotions, FoundationNavigation, FoundationTypography, FoundationVoiceAndTone

urlpatterns = [
    url(r'^$', FoundationIndex.as_view()),
    url(r'^colors/', FoundationColors.as_view()),
    url(r'^grid/', FoundationGrid.as_view()),
    #url(r'^blocks/', DesignBlocks.as_view()),
    url(r'^icons/', FoundationIcons.as_view()),
    url(r'^layout/', FoundationLayout.as_view()),
    url(r'^loading/', FoundationLayout.as_view()),
    url(r'^navigation/', FoundationNavigation.as_view()),
    url(r'^motions/', FoundationMotions.as_view()),
    url(r'^typography/', FoundationTypography.as_view()),
    url(r'^voice-and-tone/', FoundationVoiceAndTone.as_view()),
]