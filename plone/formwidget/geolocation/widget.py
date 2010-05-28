from zope.interface import implementer, implementsOnly
from zope.component import adapter

from z3c.form.interfaces import IFieldWidget, IFormLayer
from z3c.form.widget import FieldWidget
from z3c.form.browser.text import TextWidget

from plone.formwidget.geolocation.interfaces import IGeolocationField, IGeolocationWidget

class GeolocationWidget(TextWidget):
    implementsOnly(IGeolocationWidget)

    klass = u'geolocation-widget'
    value = None # don't default to a string

@implementer(IFieldWidget)
@adapter(IGeolocationField, IFormLayer)
def GeolocationFieldWidget(field, request):
    return FieldWidget(field, GeolocationWidget(request))
