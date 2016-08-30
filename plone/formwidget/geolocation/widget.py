# -*- coding: utf-8 -*-
from plone.formwidget.geolocation.interfaces import IGeolocationField
from plone.formwidget.geolocation.interfaces import IGeolocationWidget
from plone.uuid.interfaces import IUUID
from Products.CMFPlone.utils import safe_unicode
from z3c.form.browser.text import TextWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.component import queryMultiAdapter
from zope.interface import implementer
from zope.interface import implementer_only

import json


@implementer_only(IGeolocationWidget)
class GeolocationWidget(TextWidget):

    klass = u'geolocation-widget'
    value = None

    def update(self):
        super(GeolocationWidget, self).update()
        if self.value is None and self.mode == 'input':
            self.value = self._default_loc()

    @property
    def id_input_lat(self):
        return u'{0}_latitude'.format(self.id)

    @property
    def id_input_lng(self):
        return u'{0}_longitude'.format(self.id)

    @property
    def data_geojson(self):
        """Return the geo location as GeoJSON string.
        """
        coordinates = self.value
        if not coordinates:
            return

        title = getattr(self.context, 'title', '')
        description = getattr(self.context, 'description', '')

        geo_json = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'type': 'Feature',
                    'properties': {
                        'popup': u'<h3>{0}</h3><p>{1}</p>'.format(
                            safe_unicode(title),
                            safe_unicode(description)
                        )
                    },
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [
                            coordinates[1],  # lng
                            coordinates[0]   # lat
                        ]
                    }
                },
            ]
        }

        if self.mode == 'input':
            properties = geo_json['features'][0]['properties']
            properties['editable'] = True
            properties['no_delete'] = True
            properties['latinput'] = u'#{0}'.format(self.id_input_lat)
            properties['lnginput'] = u'#{0}'.format(self.id_input_lng)

        return json.dumps(geo_json)

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
