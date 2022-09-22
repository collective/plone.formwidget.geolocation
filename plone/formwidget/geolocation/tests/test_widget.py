# -*- coding: utf-8 -*-

from io import StringIO
from plone.api.portal import set_registry_record
from plone.formwidget.geolocation.interfaces import IGeolocationWidget
from plone.formwidget.geolocation.testing import GEOLOCATION_INTEGRATION_TESTING
from plone.formwidget.geolocation.tests.utils import IDummyGeolocation
from plone.formwidget.geolocation.widget import GeolocationFieldWidget
from plone.formwidget.geolocation.widget import GeolocationWidget
from z3c.form.widget import WidgetTemplateFactory
from zope.configuration.xmlconfig import XMLConfig
from zope.configuration.xmlconfig import xmlconfig
from zope.interface import implementer
from zope.interface import Interface
from zope.pagetemplate.interfaces import IPageTemplate

import json
import mock
import os
import plone.formwidget.geolocation
import unittest
import zope.browserpage
import zope.component


zcml_wrapper = """<configure
   xmlns='http://namespaces.zope.org/zope'
   xmlns:browser='http://namespaces.zope.org/browser'
   i18n_domain='zope'>
   %s
</configure>"""


class IDummyContent(Interface):
    """ """


@implementer(IDummyContent)
class DummyContent(object):
    """ """

    title = "Title"
    description = "Description"


class TestWidget(unittest.TestCase):

    layer = GEOLOCATION_INTEGRATION_TESTING

    def setUp(self):
        self.request = self.layer["request"]
        XMLConfig("meta.zcml", zope.browserpage)()

    def test_value(self):
        widget = GeolocationWidget(self.request)
        widget.id = widget.name = "geolocation"
        widget.request[widget.name] = (50.0, 5.0)
        widget.update()
        self.assertEqual(widget.value, (50.0, 5.0))

        widget.request[widget.name] = None
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
        widget.context = DummyContent()
        widget.request[widget.name] = None
        widget.update()
        self.assertEqual(widget.data_geojson, None)

        widget.request[widget.name] = (50.0, None)
        widget.update()
        self.assertEqual(widget.data_geojson, None)

        widget.request[widget.name] = (50.0, 5.0)
        widget.update()
        json_result = json.loads(widget.data_geojson)
        feature = json_result["features"][0]
        coordinates = feature["geometry"]["coordinates"]
        self.assertEqual(coordinates, [5.0, 50.0])

    def test_default_loc(self):
        widget = GeolocationWidget(self.request)
        widget.id = widget.name = "geolocation"
        widget.request[widget.name] = None

        widget.update()
        self.assertEqual(widget._default_loc(), (None, None))

        set_registry_record("geolocation.default_latitude", 70.0)
        set_registry_record("geolocation.default_longitude", 7.0)
        widget.update()
        self.assertEqual(widget._default_loc(), (70.0, 7.0))

        set_registry_record("geolocation.use_default_geolocation_as_value", False)
        widget.update()
        self.assertEqual(widget._default_loc(), (None, None))

    def test_render(self):
        widget = GeolocationWidget(self.request)
        widget.id = widget.name = "geolocation"
        self.request[widget.name] = (50.0, 5.0)
        widget.request = self.request
        widget.update()

        path = os.path.join(
            os.path.dirname(plone.formwidget.geolocation.__file__),
            "geolocation_input.pt",
        )
        zope.component.provideAdapter(
            WidgetTemplateFactory(path, "text/html"),
            (None, None, None, None, IGeolocationWidget),
            IPageTemplate,
            name=widget.mode,
        )
        render = widget.render()
        self.assertIn(
            'id="geolocation_latitude" name="geolocation:tuple" value="50.0"', render
        )
        self.assertIn(
            'id="geolocation_longitude" name="geolocation:tuple" value="5.0"', render
        )

        widget.mode = "display"
        path = os.path.join(
            os.path.dirname(plone.formwidget.geolocation.__file__),
            "geolocation_display.pt",
        )
        zope.component.provideAdapter(
            WidgetTemplateFactory(path, "text/html"),
            (None, None, None, None, IGeolocationWidget),
            IPageTemplate,
            name=widget.mode,
        )
        render = widget.render()
        self.assertNotIn("input", render)
        self.assertIn("pat-leaflet map", render)

        widget.request[widget.name] = (None, None)
        widget.update()
        render = widget.render()
        self.assertNotIn("pat-leaflet map", render)

    def test_popup(self):
        widget = GeolocationWidget(self.request)
        widget.id = widget.name = "geolocation"
        widget.context = DummyContent()
        widget.request[widget.name] = (50.0, 5.0)
        widget.update()
        json_result = json.loads(widget.data_geojson)
        feature = json_result["features"][0]
        popup = feature["properties"]["popup"]
        self.assertEqual(popup.strip(), "<h3>Title</h3\n ><p>Description</p>")

        template_path = os.path.join(os.path.dirname(__file__), "test_popup.pt")
        zcml = (
            """
            <browser:page
                name="geolocation-geojson-popup"
                for="plone.formwidget.geolocation.tests.test_widget.IDummyContent"
                class="plone.formwidget.geolocation.popup.PopupView"
                template="%s"
                permission="zope.Public"
                />
            """
            % template_path
        )
        xmlconfig(StringIO(zcml_wrapper % zcml))
        widget.update()
        json_result = json.loads(widget.data_geojson)
        feature = json_result["features"][0]
        popup = feature["properties"]["popup"]
        self.assertEqual(popup.strip(), "<span>Foo Bar</span>Title")

    @mock.patch("plone.formwidget.geolocation.widget.GeolocationWidget")
    def test_field_widget(self, GeolocationWidget):
        field = IDummyGeolocation.get("geolocation")
        GeolocationFieldWidget(field, self.request)
        self.assertTrue(GeolocationWidget.called)
