from plone.formwidget.geolocation.testing import GEOLOCATION_INTEGRATION_TESTING
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

import unittest


class TestVocabularies(unittest.TestCase):
    layer = GEOLOCATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]

    def test_vocabulary_map_layers(self):
        factory = getUtility(
            IVocabularyFactory, "plone.formwidget.geolocation.vocabularies.map_layers"
        )
        vocabulary = factory(self.portal)
        self.assertEqual(len(vocabulary), 23)
        # providers that are gone from leaflet-providers leave the map empty
        self.assertNotIn("OpenStreetMap.BlackAndWhite", vocabulary)
        self.assertNotIn("Stamen.TonerLite", vocabulary)
        self.assertIn("CartoDB.Positron", vocabulary)

    def test_valid_map_layers(self):
        from plone.formwidget.geolocation.vocabularies import valid_map_layers

        # stored layers that are no longer offered are dropped
        self.assertEqual(
            valid_map_layers(
                ["OpenStreetMap.Mapnik", "OpenStreetMap.BlackAndWhite"],
                "OpenStreetMap.Mapnik",
            ),
            (["OpenStreetMap.Mapnik"], "OpenStreetMap.Mapnik"),
        )
        # a stale default falls back to the first remaining layer ...
        self.assertEqual(
            valid_map_layers(["Esri.WorldImagery"], "Stamen.TonerLite"),
            (["Esri.WorldImagery"], "Esri.WorldImagery"),
        )
        # ... or to the package default
        self.assertEqual(
            valid_map_layers(None, "Stamen.TonerLite"),
            ([], "OpenStreetMap.Mapnik"),
        )
