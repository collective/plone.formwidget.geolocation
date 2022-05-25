# -*- coding: utf-8 -*-

from plone.api.portal import set_registry_record
from plone.formwidget.geolocation.interfaces import IGeolocationWidget
from plone.formwidget.geolocation.testing import GEOLOCATION_INTEGRATION_TESTING
from plone.formwidget.geolocation.widget import GeolocationWidget
from z3c.form.widget import WidgetTemplateFactory
from zope.pagetemplate.interfaces import IPageTemplate

import json
import os
import unittest2 as unittest
import zope.component


class TestWidget(unittest.TestCase):

    layer = GEOLOCATION_INTEGRATION_TESTING

    def setUp(self):
        self.request = self.layer["request"]

    def test_bundle_on_request(self):
        GeolocationWidget(self.request)
        bundles = getattr(self.request, "enabled_bundles", [])
        self.assertListEqual(bundles, ["bundle-leaflet"])

    def test_value(self):
        widget = GeolocationWidget(self.request)
        widget.id = widget.name = "geolocation"
        widget.request = {widget.name: (50.0, 5.0)}
        widget.update()
        self.assertEqual(widget.value, (50.0, 5.0))

        widget.request = {widget.name: None}
        widget.update()
        self.assertEqual(widget.value, (None, None))

        widget.mode = "input"
        widget.update()
        self.assertEqual(widget.value, (None, None))

        set_registry_record("geolocation.default_latitude", 70.0)
        set_registry_record("geolocation.default_longitude", 7.0)
        widget.update()
        self.assertEqual(widget.value, (70.0, 7.0))

    def test_data_geojson(self):
        widget = GeolocationWidget(self.request)
        widget.id = widget.name = "geolocation"
        widget.request = {widget.name: None}
        widget.update()
        self.assertEqual(widget.data_geojson, None)

        widget.request = {widget.name: (50.0, None)}
        widget.update()
        self.assertEqual(widget.data_geojson, None)

        widget.request = {widget.name: (50.0, 5.0)}
        widget.update()
        json_result = json.loads(widget.data_geojson)
        coordinates = json_result["features"][0]["geometry"]["coordinates"]
        self.assertEqual(coordinates, [5.0, 50.0])

    def test_default_loc(self):
        widget = GeolocationWidget(self.request)
        widget.id = widget.name = "geolocation"
        widget.request = {widget.name: None}

        widget.update()
        self.assertEqual(widget._default_loc(), (None, None))

        set_registry_record("geolocation.default_latitude", 70.0)
        set_registry_record("geolocation.default_longitude", 7.0)
        widget.update()
        self.assertEqual(widget._default_loc(), (70.0, 7.0))

    def test_render(self):
        widget = GeolocationWidget(self.request)
        widget.id = widget.name = "geolocation"
        widget.request = {widget.name: (50.0, 5.0)}
        widget.update()
        p = os.path.abspath("..")
        zope.component.provideAdapter(
            WidgetTemplateFactory("../geolocation_input.pt", "text/html"),
            (None, None, None, None, IGeolocationWidget),
            IPageTemplate,
            name=widget.mode,
        )
        widget.render()
