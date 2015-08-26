from django.test import TestCase, RequestFactory

from ..views import ListCreateDataView, ListUpdateDataView, ListDeleteDateView
from ..models import ListData

from datetime import date, datetime


class TestViewObjectCreate(TestCase):

    def setUp(self):
        pass

    def test_object_create(self):
        view = ListCreateDataView.as_view()

        self.assertEqual(ListData.objects.count(), 0)

        request = RequestFactory().get('/')
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ListData.objects.count(), 0)

        data = {
            'name': 'Name',
            'boolean': True,
            'date': date.today(),
            'datetime': datetime.now(),
            'decimal': '5',
        }

        request = RequestFactory().post('/', data=data)
        response = view(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ListData.objects.count(), 1)


class TestViewObjectUpdate(TestCase):

    def setUp(self):
        pass

    def test_object_update(self):
        view = ListUpdateDataView.as_view()

        object = ListData.objects.create(
             name='Name',
             boolean=True,
             date=date.today(),
             datetime=datetime.now(),
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
            'date': date.today(),
            'datetime': datetime.now(),
            'decimal': '800',
        }

        request = RequestFactory().post('/', data=data)
        response = view(request, pk=object.pk)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ListData.objects.count(), 1)

        object_updated = ListData.objects.get(pk=object.pk)

        self.assertEqual(object_updated.name, 'Name - Updated')
        self.assertEqual(object_updated.decimal, 800)


class TestViewObjectDelete(TestCase):

    def setUp(self):
        pass

    def test_object_delete(self):
        view = ListDeleteDateView.as_view()

        object = ListData.objects.create(
             name='Name',
             boolean=True,
             date=date.today(),
             datetime=datetime.now(),
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