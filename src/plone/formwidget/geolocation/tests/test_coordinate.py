"""Tests for the locale independent coordinate widget of the control panel."""

from plone.formwidget.geolocation.controlpanel import GeolocationControlPanelForm
from plone.formwidget.geolocation.converter import CoordinateDataConverter
from plone.formwidget.geolocation.testing import GEOLOCATION_INTEGRATION_TESTING
from plone.formwidget.geolocation.widget import CoordinateWidget
from z3c.form.converter import FormatterValidationError
from z3c.form.interfaces import IDataConverter
from zope import schema
from zope.component import getMultiAdapter
from zope.i18n.locales import locales

import unittest


class TestCoordinateDataConverter(unittest.TestCase):

    def setUp(self):
        self.field = schema.Float(required=False)
        self.converter = CoordinateDataConverter(self.field, None)

    def test_to_field_value_accepts_point_and_comma(self):
        self.assertEqual(self.converter.toFieldValue("47.4064329"), 47.4064329)
        self.assertEqual(self.converter.toFieldValue("47,4064329"), 47.4064329)
        self.assertEqual(self.converter.toFieldValue("9.7"), 9.7)
        self.assertEqual(self.converter.toFieldValue(" -0,5 "), -0.5)
        self.assertEqual(self.converter.toFieldValue("12"), 12.0)

    def test_to_field_value_empty(self):
        self.assertIsNone(self.converter.toFieldValue(""))
        self.assertIsNone(self.converter.toFieldValue("  "))
        self.assertIsNone(self.converter.toFieldValue(None))

    def test_to_field_value_invalid(self):
        for value in ("abc", "47.406,432", "1.2.3"):
            with self.assertRaises(FormatterValidationError):
                self.converter.toFieldValue(value)

    def test_to_widget_value_keeps_precision(self):
        self.assertEqual(self.converter.toWidgetValue(47.4064329), "47.4064329")
        self.assertEqual(self.converter.toWidgetValue(9.7), "9.7")
        self.assertEqual(self.converter.toWidgetValue(0.0), "0.0")
        self.assertEqual(self.converter.toWidgetValue(None), "")


class TestControlPanel(unittest.TestCase):

    layer = GEOLOCATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        # the bug only shows with a locale that uses "." for grouping
        self.request._locale = locales.getLocale("de")

    def form(self, **values):
        for name, value in values.items():
            self.request.form[f"form.widgets.{name}"] = value
        form = GeolocationControlPanelForm(self.portal, self.request)
        form.update()
        return form

    def test_coordinate_widgets_used(self):
        form = self.form()
        for name in ("default_latitude", "default_longitude"):
            widget = form.widgets[name]
            self.assertIsInstance(widget, CoordinateWidget)
            converter = getMultiAdapter((widget.field, widget), IDataConverter)
            self.assertIsInstance(converter, CoordinateDataConverter)
        # the other number fields keep the default widget
        self.assertNotIsInstance(form.widgets["default_input_zoom"], CoordinateWidget)

    def test_extract_coordinates_german_locale(self):
        form = self.form(default_latitude="47,4064329", default_longitude="9.7")
        data, errors = form.extractData()
        self.assertEqual(errors, ())
        self.assertEqual(data["default_latitude"], 47.4064329)
        self.assertEqual(data["default_longitude"], 9.7)

    def test_invalid_coordinate_reports_error(self):
        form = self.form(default_latitude="abc")
        data, errors = form.extractData()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0].widget.name, "form.widgets.default_latitude")

    def test_display_value_not_localized(self):
        form = self.form()
        widget = form.widgets["default_latitude"]
        converter = getMultiAdapter((widget.field, widget), IDataConverter)
        self.assertEqual(converter.toWidgetValue(47.4064329), "47.4064329")
