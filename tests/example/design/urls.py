from django.conf.urls import url

from .views import DesignColors, DesignGrid, DesignIcons, DesignLayout, DesignMotions, DesignTypography

urlpatterns = [
    url(r'^colors/', DesignColors.as_view()),
    url(r'^grid/', DesignGrid.as_view()),
    url(r'^icons/', DesignIcons.as_view()),
    url(r'^layout/', DesignLayout.as_view()),
    url(r'^motions/', DesignMotions.as_view()),
    url(r'^typography/', DesignTypography.as_view()),
]