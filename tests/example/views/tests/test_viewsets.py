from datetime import date, datetime

from django.test import TestCase, RequestFactory
from django.utils import timezone

from example.views.views import ListDataModelView
from example.views.models import ListData

class TestViewSet(TestCase):

    def setUp(self):
        pass

    def test_viewset_urls(self):
        view = ListDataModelView()
        object = ListData.objects.create(
             name='Name',
             boolean=True,
             date=date.today(),
             datetime=timezone.now(),
             decimal=5
        )

        self.assertEqual(len(view.urls), 4)

        response = self.client.get('/views/listdata/')
        self.assertEqual(response.status_code, 200)

        response =  self.client.get('/views/listdata/create/')
        self.assertEqual(response.status_code, 200)

        response =  self.client.get('/views/listdata/%s/update/' % object.pk)
        self.assertEqual(response.status_code, 200)

        response =  self.client.get('/views/listdata/%s/delete/' % object.pk)
        self.assertEqual(response.status_code, 200)
