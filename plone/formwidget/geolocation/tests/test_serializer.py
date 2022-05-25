# -*- coding: utf-8 -*-

from plone.formwidget.geolocation.testing import GEOLOCATION_INTEGRATION_TESTING
from plone.dexterity.content import DexterityContent
from plone.dexterity.utils import iterSchemata
from plone.formwidget.geolocation.field import GeolocationField
from plone.formwidget.geolocation.geolocation import Geolocation
from plone.restapi.interfaces import IFieldSerializer
from plone.supermodel import model
from zope.component import getMultiAdapter
from zope.interface import implementer

import unittest2 as unittest


class IDummyGeolocation(model.Schema):
    """"""

    geolocation = GeolocationField(title=u"Geolocation")


@implementer(IDummyGeolocation)
class DummyContent(DexterityContent):
    """"""


class TestSerializer(unittest.TestCase):

    layer = GEOLOCATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
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
