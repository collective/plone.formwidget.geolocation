# -*- coding: utf-8 -*-
from plone.formwidget.geolocation.geolocation import Geolocation
from plone.formwidget.geolocation.interfaces import IGeolocation
from plone.formwidget.geolocation.interfaces import IGeolocationField
from plone.formwidget.geolocation.interfaces import IGeolocationWidget
from z3c.form.converter import BaseDataConverter
from zope.component import adapter


@adapter(IGeolocationField, IGeolocationWidget)
class GeolocationConverter(BaseDataConverter):
    """Converts from a 2-tuple to a Geolocation
    """

    def toWidgetValue(self, value):
        if value:
            return (value.latitude, value.longitude)

    def toFieldValue(self, value):
        if value is None or value == ('0', '0'):
            return self.field.missing_value

        if IGeolocation.providedBy(value):
            return value

        return Geolocation(value[0], value[1])
