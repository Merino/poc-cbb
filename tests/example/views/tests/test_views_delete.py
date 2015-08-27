from datetime import date, datetime

from django.test import TestCase, RequestFactory
from django.utils import timezone

from example.views.views import ListCreateDataView, ListUpdateDataView, ListDeleteDateView
from example.views.models import ListData


class TestViewDetailDelete(TestCase):

    def setUp(self):
        pass

    def test_view_delete(self):
        view = ListDeleteDateView.as_view()

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
        }

        request = RequestFactory().post('/', data=data)
        response = view(request, pk=object.pk)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ListData.objects.count(), 0)