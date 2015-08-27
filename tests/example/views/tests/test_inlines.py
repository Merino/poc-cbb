
import os
import shutil
from django.test import TestCase


from panels import models
#from example.views.models import NestedA, NestedB, NestedC, NestedD
#
#
# class TestViewInline(TestCase):
#
#     def setUp(self):
#         pass
#
#     def test_get_request(self):
#         response = self.client.get('/views/inline/single/')
#         self.assertEqual(response.status_code, 200)
#
#         print response
#
#     def test_post_request(self):
#
#         self.assertEqual(NestedA.objects.count(), 0)
#         self.assertEqual(NestedB.objects.count(), 0)
#
#         data = {
#             'name': 'Value One',
#             'form-TOTAL_FORMS': '1',
#             'form-INITIAL_FORMS': '0',
#             'form-MAX_NUM_FORMS': '1000',
#             'form-0-name': 'name',
#             'form-0-nested_a': 1,
#         }
#
#         response = self.client.post('/views/inline/single/', data=data)
#         self.assertEqual(response.status_code, 200)
#
#         print response
#
#         self.assertEqual(NestedA.objects.count(), 1)
#         self.assertEqual(NestedB.objects.count(), 0)
