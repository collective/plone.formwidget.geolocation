from plone.formwidget.geolocation.geolocation import Geolocation

import unittest


class TestGeolocation(unittest.TestCase):
    def test_geolocation(self):
        geolocation = Geolocation()
        self.assertEqual(geolocation.latitude, 0.0)
        self.assertEqual(geolocation.longitude, 0.0)

        geolocation = Geolocation("", "")
        self.assertEqual(geolocation.latitude, None)
        self.assertEqual(geolocation.longitude, None)

        geolocation = Geolocation(50.0, 5.0)
        self.assertEqual(geolocation.latitude, 50.0)
        self.assertEqual(geolocation.longitude, 5.0)
