from datetime import date, datetime

from django.test import TestCase, RequestFactory
from django.utils import timezone

from example.views.views import ListCreateDataView, ListUpdateDataView, ListDeleteDateView
from example.views.models import ListData


class TestViewDetailUpdate(TestCase):

    def setUp(self):
        pass

    def test_view_update(self):
        view = ListUpdateDataView.as_view()

        object = ListData.objects.create(
             name='Name',
             boolean=True,
             date=date.today(),
             datetime=timezone.now(),
             decimal=5
        )

        self.assertEqual(ListData.objects.count(), 1)

        request = RequestFactory().get('/')
        response = view(request, pk=object.pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ListData.objects.count(), 1)

        data = {
            'id': object.pk,
            'name': 'Name - Updated',
            'boolean': True,
            'date': '2015-08-27',
            'datetime': '2015-08-27 07:53:03',
            'decimal': '800',
        }

        request = RequestFactory().post('/', data=data)
        response = view(request, pk=object.pk)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ListData.objects.count(), 1)

        object_updated = ListData.objects.get(pk=object.pk)

        self.assertEqual(object_updated.name, 'Name - Updated')
        self.assertEqual(object_updated.decimal, 800)