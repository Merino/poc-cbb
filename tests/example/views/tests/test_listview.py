from django.test import TestCase

from example.views.views import ListDataModelView
from example.views.models import ListData

class TestListView(TestCase):

    def setUp(self):
        pass

    def test_view_list_empty(self):
        pass

    def test_view_list_results(self):
        pass

    def test_view_list_paginate(self):
        pass

    def test_view_list_ordering(self):
        pass


class TestListViewSearch(TestCase):

    def setUp(self):
        pass

    def test_view_list_search_single_field(self):
        pass

    def test_view_list_search_multiple_fields(self):
        pass

    def test_view_list_search_multiple_values(self):
        pass

    def test_view_list_search_relation_field(self):
        pass


class TestListViewFacets(TestCase):

    def setUp(self):
        pass

    def test_view_list_facets_single_filter(self):
        pass

    def test_view_list_facets_multiple_filters(self):
        pass

    def test_view_list_facets_multiple_value_filter(self):
        pass


class TestListViewActions(TestCase):

    def setUp(self):
        pass

    def test_view_list_action_single_item(self):
        pass

    def test_view_list_action_multiple_items(self):
        pass

    def test_view_list_action_with_form(self):
        pass