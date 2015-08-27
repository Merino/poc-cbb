#
# import os
# import shutil
# from django.test import TestCase
#
#
# from panels import models
# from example.views.models import NestedA, NestedB, NestedC, NestedD
#
#
# class TestPanels(TestCase):
#
#     def setUp(self):
#         pass
#
#     def test_something(self):
#
#         self.assertEqual(NestedA.objects.count(), 0)
#
#         response = self.client.get('/views/form/single/')
#
#         self.assertEqual(response.status_code, 200)
#
#         data = {
#             'name': 'Value One'
#         }
#
#         response = self.client.post('/views/form/single/', data=data)
#
#         self.assertEqual(response.status_code, 302)
#
#         self.assertEqual(NestedA.objects.count(), 1)
#
#     def tearDown(self):
#         pass
