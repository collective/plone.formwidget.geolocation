# -*- coding: utf-8 -*-

from plone.formwidget.geolocation.geolocation import Geolocation
from plone.formwidget.geolocation.testing import GEOLOCATION_INTEGRATION_TESTING
from plone.formwidget.geolocation.tests.utils import DummyContent
from plone.formwidget.geolocation.tests.utils import IDummyGeolocation
from plone.restapi.interfaces import IFieldSerializer
from zope.component import getMultiAdapter

import unittest


class TestSerializer(unittest.TestCase):

    layer = GEOLOCATION_INTEGRATION_TESTING

    def setUp(self):
        self.request = self.layer["request"]

    def test_serializer(self):
        content = DummyContent()

        content.geolocation = None
        field = IDummyGeolocation.get("geolocation")
        serializer = getMultiAdapter((field, content, self.request), IFieldSerializer)
        result = serializer()
        self.assertEqual(result, {})

        content.geolocation = Geolocation()
        field = IDummyGeolocation.get("geolocation")
        serializer = getMultiAdapter((field, content, self.request), IFieldSerializer)
        result = serializer()
        self.assertEqual(result, {"latitude": 0.0, "longitude": 0.0})

        content.geolocation = Geolocation(50.0, 5.0)
        serializer = getMultiAdapter((field, content, self.request), IFieldSerializer)
        result = serializer()
        self.assertEqual(result, {"latitude": 50.0, "longitude": 5.0})
