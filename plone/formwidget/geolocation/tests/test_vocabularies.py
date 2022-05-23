# -*- coding: utf-8 -*-

from plone import api
from plone.formwidget.geolocation.testing import GEOLOCATION_INTEGRATION_TESTING
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

import unittest2 as unittest


class TestVocabularies(unittest.TestCase):

    layer = GEOLOCATION_INTEGRATION_TESTING

    def test_vocabulary_map_layers(self):
        factory = getUtility(IVocabularyFactory, "plone.formwidget.geolocation.vocabularies.map_layers")
        vocabulary = factory(api.portal.get())
        self.assertEqual(len(vocabulary), 28)