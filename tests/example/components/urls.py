from django.conf.urls import url

from .views import ComponentIndexView, ComponentNotificationView, ComponentFormInputView, ComponentFormLayoutView, \
    ComponentFormValidationView, ComponentButtonView, ComponentTableView, ComponentLabelView, ComponentHeaderView, \
    ComponentCardsView, ComponentBreadcrumbView

urlpatterns = [
    url(r'^$', ComponentIndexView.as_view()),
    url(r'^notification/', ComponentNotificationView.as_view()),
    url(r'^form-input/', ComponentFormInputView.as_view()),
    url(r'^form-validation/', ComponentFormValidationView.as_view()),
    url(r'^form-layout/', ComponentFormLayoutView.as_view()),
    url(r'^button/', ComponentButtonView.as_view()),
    url(r'^header/', ComponentHeaderView.as_view()),
    url(r'^table/', ComponentTableView.as_view()),
    url(r'^label/', ComponentLabelView.as_view()),
     url(r'^cards/', ComponentCardsView.as_view()),
    url(r'^breadcrumb', ComponentBreadcrumbView.as_view()),
]