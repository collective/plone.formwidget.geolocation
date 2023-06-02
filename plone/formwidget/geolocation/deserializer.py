from plone.dexterity.interfaces import IDexterityContent
from plone.formwidget.geolocation.geolocation import Geolocation
from plone.formwidget.geolocation.interfaces import IGeolocationField
from plone.restapi.deserializer.dxfields import DefaultFieldDeserializer
from plone.restapi.interfaces import IFieldDeserializer
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface


@adapter(IGeolocationField, IDexterityContent, Interface)
@implementer(IFieldDeserializer)
class GeolocationDeserializer(DefaultFieldDeserializer):
    def __call__(self, value):
        if not isinstance(value, dict):
            raise ValueError(f"Invalid geolocation dict: {value}")

        if "latitude" not in value or "longitude" not in value:
            raise ValueError("Geolocation dict must have latitude & longitude keys")

        return Geolocation(value["latitude"], value["longitude"])
