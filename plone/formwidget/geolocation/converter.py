from plone.formwidget.geolocation.geolocation import Geolocation
from plone.formwidget.geolocation.bounds import Bounds
from plone.formwidget.geolocation.interfaces import IGeolocation
from plone.formwidget.geolocation.interfaces import IGeolocationField
from plone.formwidget.geolocation.interfaces import IGeolocationWidget
from z3c.form.converter import BaseDataConverter
from zope.component import adapts


class GeolocationConverter(BaseDataConverter):
    """Converts from a 2-tuple to a Geolocation
    """
    adapts(IGeolocationField, IGeolocationWidget)

    def toWidgetValue(self, value):
        if value:
            bounds = getattr(value, 'bounds', Bounds(0, 0, 0, 0))
            return (
                value.latitude,
                value.longitude,
                bounds.south,
                bounds.west,
                bounds.north,
                bounds.east,
            )

    def toFieldValue(self, value):
        if value is None or value == ('0', '0', '0', '0', '0', '0'):
            return self.field.missing_value

        if IGeolocation.providedBy(value):
            return value

        bounds = Bounds(*value[2:])

        return Geolocation(value[0], value[1], bounds)
