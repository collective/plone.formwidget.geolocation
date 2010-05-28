from zope import schema
from zope.interface import implements
from plone.formwidget.geolocation.interfaces import IGeolocationField, IGeolocation
from plone.formwidget.geolocation.geolocation import Geolocation

class GeolocationField(schema.Object):
    implements(IGeolocationField)
    
    _type = Geolocation
    schema = IGeolocation
    
    def __init__(self, **kw):
        super(GeolocationField, self).__init__(schema=self.schema, **kw)
