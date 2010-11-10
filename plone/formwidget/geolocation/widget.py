from zope.interface import implementer, implementsOnly
from zope.component import adapter, getMultiAdapter

from z3c.form.interfaces import IFieldWidget, IFormLayer
from z3c.form.widget import FieldWidget
from z3c.form.browser.text import TextWidget

from plone.formwidget.geolocation.interfaces import IGeolocationField, IGeolocationWidget


class GeolocationWidget(TextWidget):
    implementsOnly(IGeolocationWidget)

    klass = u'geolocation-widget'
    value = None
    
    def update(self):
        super(GeolocationWidget, self).update()
        if self.value is None:
            self.value = self._default_loc()
    
    def _default_loc(self):
        config = getMultiAdapter((self.context, self.request), 
                                    name="maps_configuration")
        return tuple(config.default_location)


@implementer(IFieldWidget)
@adapter(IGeolocationField, IFormLayer)
def GeolocationFieldWidget(field, request):
    return FieldWidget(field, GeolocationWidget(request))
