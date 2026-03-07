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
        self.assertEqual(len(vocabulary), 28)
