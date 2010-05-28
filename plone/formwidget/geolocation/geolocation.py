from zope.interface import implements
from plone.formwidget.geolocation.interfaces import IGeolocation

class Geolocation(object):
    implements(IGeolocation)

    def __init__(self, latitude=0, longitude=0):
        self.latitude = float(latitude)
        self.longitude = float(longitude)
