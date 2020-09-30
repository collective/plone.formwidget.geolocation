# -*- coding: utf-8 -*-
from plone.formwidget.geolocation.interfaces import IGeolocation
from zope.interface import implementer


@implementer(IGeolocation)
class Geolocation(object):
    def __init__(self, latitude=0, longitude=0):
        try:
            self.latitude = float(latitude)
        except ValueError:
            self.latitude = None
        try:
            self.longitude = float(longitude)
        except ValueError:
            self.longitude = None
