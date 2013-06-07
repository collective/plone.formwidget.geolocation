from zope.interface import implementer, implementsOnly
from zope.component import adapter, queryMultiAdapter

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
        if self.value is None and self.mode == 'input':
            self.value = self._default_loc()
    
    def _default_loc(self):
        config = queryMultiAdapter((self.context, self.request), 
                                  name="maps_configuration", default=None)
        default = ret = (0.0, 0.0)
        if config and hasattr(config, 'default_location'):
            ret = config.default_location
            if isinstance(ret, basestring):
                ret = ret.split(',')
        if len(ret) != 2:
            return default
        return (float(ret[0]), float(ret[1]))


@implementer(IFieldWidget)
@adapter(IGeolocationField, IFormLayer)
def GeolocationFieldWidget(field, request):
    return FieldWidget(field, GeolocationWidget(request))
