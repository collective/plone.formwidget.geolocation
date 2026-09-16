from plone.formwidget.geolocation import _
from plone.formwidget.geolocation.geolocation import Geolocation
from plone.formwidget.geolocation.interfaces import ICoordinateWidget
from plone.formwidget.geolocation.interfaces import IGeolocation
from plone.formwidget.geolocation.interfaces import IGeolocationField
from plone.formwidget.geolocation.interfaces import IGeolocationWidget
from z3c.form.converter import BaseDataConverter
from z3c.form.converter import FormatterValidationError
from zope.component import adapter
from zope.schema.interfaces import IFloat


@adapter(IGeolocationField, IGeolocationWidget)
class GeolocationConverter(BaseDataConverter):
    """Converts from a 2-tuple to a Geolocation"""

    def toWidgetValue(self, value):
        if value and value.latitude is not None and value.longitude is not None:
            return (value.latitude, value.longitude)

    def toFieldValue(self, value):
        if IGeolocation.providedBy(value):
            return value

        if value is None or value == ("0", "0") or "" in value:
            return self.field.missing_value

        return Geolocation(value[0], value[1])


@adapter(IFloat, ICoordinateWidget)
class CoordinateDataConverter(BaseDataConverter):
    """Locale independent converter for latitude/longitude floats.

    Always renders the full precision with a decimal point and no grouping,
    accepts both ``.`` and ``,`` as decimal separator on input.
    """

    errorMessage = _(
        "error_invalid_coordinate",
        default="The entered value is not a valid coordinate.",
    )

    def toWidgetValue(self, value):
        if value is None or value == self.field.missing_value:
            return ""
        return repr(float(value))

    def toFieldValue(self, value):
        value = (value or "").strip()
        if not value:
            return self.field.missing_value
        try:
            return float(value.replace(",", "."))
        except ValueError:
            raise FormatterValidationError(self.errorMessage, value)
