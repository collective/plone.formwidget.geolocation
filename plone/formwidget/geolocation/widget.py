from Products.CMFPlone.utils import safe_unicode
from plone.formwidget.geolocation.interfaces import IGeolocationField
from plone.formwidget.geolocation.interfaces import IGeolocationWidget
from z3c.form.browser.text import TextWidget
from z3c.form.interfaces import IFieldWidget, IFormLayer
from z3c.form.widget import FieldWidget
from zope.component import adapter, queryMultiAdapter
from zope.interface import implementer, implementsOnly
import json


class GeolocationWidget(TextWidget):
    implementsOnly(IGeolocationWidget)

    klass = u'geolocation-widget'
    value = None

    def update(self):
        super(GeolocationWidget, self).update()
        if self.value is None and self.mode == 'input':
            self.value = self._default_loc()

    def json_value(self):
        title = getattr(self.context, 'title', '')
        description = getattr(self.context, 'description', '')
        return json.dumps([{
            'lat': self.value[0],
            'lng': self.value[1],
            'bounds': {
                'south': self.value[2],
                'west': self.value[3],
                'north': self.value[4],
                'east': self.value[5]
            },
            'popup': u'<h3>{0}</h3><p>{1}</p>'.format(
                safe_unicode(title),
                safe_unicode(description)
            )
        }])

    def _default_loc(self):
        config = queryMultiAdapter((self.context, self.request),
                                   name="maps_configuration", default=None)
        default = ret = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        if config and hasattr(config, 'default_location'):
            ret = config.default_location
            if isinstance(ret, basestring):
                ret = ret.split(',')
        if len(ret) != 2:
            return default
        return (float(ret[0]), float(ret[1]), 0.0, 0.0, 0.0, 0.0)


@implementer(IFieldWidget)
@adapter(IGeolocationField, IFormLayer)
def GeolocationFieldWidget(field, request):
    return FieldWidget(field, GeolocationWidget(request))
