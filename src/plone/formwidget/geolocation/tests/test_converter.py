from plone.formwidget.geolocation.converter import GeolocationConverter
from plone.formwidget.geolocation.geolocation import Geolocation
from unittest import mock

import unittest


def create_instance():
    field = mock.Mock()
    widget = mock.Mock()
    return GeolocationConverter(field, widget)


class TestConverter(unittest.TestCase):
    def test_instance(self):
        instance = create_instance()
        self.assertTrue(isinstance(instance, GeolocationConverter))

    def test_toWidgetValue(self):
        instance = create_instance()
        value = Geolocation()
        self.assertEqual(instance.toWidgetValue(value), (0, 0))

        value = Geolocation(None, None)
        self.assertIsNone(instance.toWidgetValue(value))

        value = Geolocation(0, 0)
        self.assertEqual(instance.toWidgetValue(value), (0, 0))

        value = Geolocation(50.0, 5.0)
        self.assertEqual(instance.toWidgetValue(value), (50.0, 5.0))

    def test_toFieldValue(self):
        instance = create_instance()
        value = None
        self.assertEqual(instance.toFieldValue(value), instance.field.missing_value)

        value = ("", "")
        self.assertEqual(instance.toFieldValue(value), instance.field.missing_value)

        value = ("0", "0")
        self.assertEqual(instance.toFieldValue(value), instance.field.missing_value)

        value = (0, 0)
        geolocation = instance.toFieldValue(value)
        self.assertEqual(geolocation.latitude, 0)
        self.assertEqual(geolocation.longitude, 0)

        value = Geolocation(50.0, 5.0)
        geolocation = instance.toFieldValue(value)
        self.assertEqual(geolocation.latitude, 50.0)
        self.assertEqual(geolocation.longitude, 5.0)

        value = (50.0, 5.0)
        geolocation = instance.toFieldValue(value)
        self.assertEqual(geolocation.latitude, 50.0)
        self.assertEqual(geolocation.longitude, 5.0)
