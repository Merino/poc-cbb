
from django.views.generic.list import ListView as ListViewBase
from django.views.generic.edit import UpdateView as UpdateViewBase


class ListView(ListViewBase):
    queryset = None

    template_name = 'panels/list.html'


class UpdateView(UpdateViewBase):
    pass