# -*- coding: utf-8 -*-
from plone.dexterity.interfaces import IDexterityContent
from plone.formwidget.geolocation.interfaces import IGeolocationField
from plone.restapi.interfaces import IFieldSerializer
from plone.restapi.serializer.converters import json_compatible
from plone.restapi.serializer.dxfields import DefaultFieldSerializer
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer


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
