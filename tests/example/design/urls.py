from django.conf.urls import url

from .views import DesignColors, DesignGrid, DesignBlocks, DesignIcons, DesignIntro, DesignLayout, DesignMotions, DesignTypography, DesignNavigation

urlpatterns = [
    url(r'^$', DesignIntro.as_view()),
    url(r'^colors/', DesignColors.as_view()),
    url(r'^grid/', DesignGrid.as_view()),
    url(r'^blocks/', DesignBlocks.as_view()),
    url(r'^icons/', DesignIcons.as_view()),
    url(r'^layout/', DesignLayout.as_view()),
    url(r'^navigation/', DesignNavigation.as_view()),
    url(r'^motions/', DesignMotions.as_view()),
    url(r'^typography/', DesignTypography.as_view()),
]