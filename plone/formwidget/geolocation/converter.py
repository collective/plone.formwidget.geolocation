# -*- coding: utf-8 -*-
from plone.dexterity.interfaces import IDexterityContent
from plone.formwidget.geolocation.geolocation import Geolocation
from plone.formwidget.geolocation.interfaces import IGeolocation
from plone.formwidget.geolocation.interfaces import IGeolocationField
from plone.formwidget.geolocation.interfaces import IGeolocationWidget
from plone.restapi.interfaces import IFieldSerializer
from plone.restapi.serializer.converters import json_compatible
from plone.restapi.serializer.dxfields import DefaultFieldSerializer
from z3c.form.converter import BaseDataConverter
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer


@adapter(IGeolocationField, IGeolocationWidget)
class GeolocationConverter(BaseDataConverter):
    """Converts from a 2-tuple to a Geolocation"""

    def toWidgetValue(self, value):
        if value:
            return (value.latitude, value.longitude)

    def toFieldValue(self, value):
        if value is None or value == ("0", "0"):
            return self.field.missing_value

        if IGeolocation.providedBy(value):
            return value

        return Geolocation(value[0], value[1])


@adapter(IGeolocationField, IDexterityContent, Interface)
@implementer(IFieldSerializer)
class GeolocationSerializer(DefaultFieldSerializer):
    def __call__(self):
        value = self.get_value()
        geolocation = {}
        if value is not None:
            geolocation["latitude"] = value.latitude
            geolocation["longitude"] = value.longitude

        return json_compatible(geolocation)
