from django.conf.urls import url

from .views import ComponentIndexView, ComponentMessagesView, ComponentFormInputView, ComponentFormLayoutView, ComponentFormValidationView, ComponentButtonView, ComponentTableView, ComponentLabelView

urlpatterns = [
    url(r'^$', ComponentIndexView.as_view()),
    url(r'^messages/', ComponentMessagesView.as_view()),
    url(r'^form-input/', ComponentFormInputView.as_view()),
    url(r'^form-validation/', ComponentFormValidationView.as_view()),
    url(r'^form-layout/', ComponentFormLayoutView.as_view()),
    url(r'^button/', ComponentButtonView.as_view()),
    url(r'^table/', ComponentTableView.as_view()),
    url(r'^label/', ComponentLabelView.as_view()),
]