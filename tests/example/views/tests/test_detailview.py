from django.test import TestCase, RequestFactory

from ..views import ListUpdateDataView
from ..models import ListData

from datetime import date, datetime


class TestDetailModelForm(TestCase):

    def setUp(self):
        pass

    def test_update_save(self):
        object = ListData.objects.create(
            name='Name',
            boolean=True,
            date=date.today(),
            datetime=datetime.now(),
            decimal=5
        )

        request = RequestFactory()

        view = ListUpdateDataView.as_view(request)

    def test_update_validation(self):
        pass

    def test_update_save_and_create(self):
        pass