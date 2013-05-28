from zope.component import adapts
from z3c.form.converter import BaseDataConverter

from plone.formwidget.geolocation.interfaces import IGeolocation, IGeolocationField, IGeolocationWidget
from plone.formwidget.geolocation.geolocation import Geolocation


class GeolocationConverter(BaseDataConverter):
    """Converts from a 2-tuple to a Geolocation
    """
    adapts(IGeolocationField, IGeolocationWidget)

    def toWidgetValue(self, value):
        return (value.latitude, value.longitude)

    def toFieldValue(self, value):
        if value is None or value == ('0', '0'):
            return self.field.missing_value

        if IGeolocation.providedBy(value):
            return value
        
        return Geolocation(value[0], value[1])
