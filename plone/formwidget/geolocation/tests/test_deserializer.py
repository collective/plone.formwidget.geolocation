# -*- coding: utf-8 -*-

from plone.formwidget.geolocation.interfaces import IGeolocation
from plone.formwidget.geolocation.testing import GEOLOCATION_INTEGRATION_TESTING
from plone.formwidget.geolocation.tests.utils import DummyContent
from plone.formwidget.geolocation.tests.utils import IDummyGeolocation
from plone.restapi.interfaces import IFieldDeserializer
from zope.component import getMultiAdapter

import unittest


class TestDeserializer(unittest.TestCase):

    layer = GEOLOCATION_INTEGRATION_TESTING

    def setUp(self):
        self.request = self.layer["request"]

    def test_deserializer(self):
        content = DummyContent()

        content.geolocation = None
        field = IDummyGeolocation.get("geolocation")
        deserializer = getMultiAdapter(
            (field, content, self.request), IFieldDeserializer
        )
        with self.assertRaises(ValueError):
            deserializer(None)
        with self.assertRaises(ValueError):
            deserializer([])
        with self.assertRaises(ValueError):
            deserializer({})

        result = deserializer({"latitude": 0.0, "longitude": 0.0})
        self.assertTrue(IGeolocation.providedBy(result))
        self.assertEqual(result.latitude, 0.0)
        self.assertEqual(result.longitude, 0.0)

        result = deserializer({"latitude": 50.0, "longitude": 5.0})
        self.assertEqual(result.latitude, 50.0)
        self.assertEqual(result.longitude, 5.0)
