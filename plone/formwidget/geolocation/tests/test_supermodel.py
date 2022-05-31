# -*- coding: utf-8 -*-

from plone.formwidget.geolocation.testing import GEOLOCATION_INTEGRATION_TESTING
from plone.formwidget.geolocation.tests.utils import IDummyGeolocation
from plone.supermodel.interfaces import IFieldExportImportHandler
from plone.supermodel.utils import prettyXML
from zope.component import getUtility

import unittest2 as unittest


SUPERMODEL_XML = """<field name="dummy" type="plone.formwidget.geolocation.GeolocationField">
  <schema>plone.formwidget.geolocation.interfaces.IGeolocation</schema>
  <title>Geolocation</title>
</field>"""


class TestSupermodel(unittest.TestCase):

    layer = GEOLOCATION_INTEGRATION_TESTING

    def test_supermodel(self):
        field = IDummyGeolocation.get("geolocation")
        field_type = "plone.formwidget.geolocation.GeolocationField"
        handler = getUtility(IFieldExportImportHandler, name=field_type)
        element = handler.write(field, "dummy", field_type)
        self.assertEqual(prettyXML(element), SUPERMODEL_XML)
