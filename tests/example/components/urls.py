from django.conf.urls import url

from .views import ComponentIndexView, ComponentMessagesView, ComponentFormView, ComponentFormButton

urlpatterns = [
    url(r'^$', ComponentIndexView.as_view()),
    url(r'^messages/', ComponentMessagesView.as_view()),
    url(r'^form/', ComponentFormView.as_view()),
    url(r'^button/', ComponentFormButton.as_view()),
]