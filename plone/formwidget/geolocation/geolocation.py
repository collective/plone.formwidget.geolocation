# -*- coding: utf-8 -*-
from plone.formwidget.geolocation.interfaces import IGeolocation
from zope.interface import implementer


@implementer(IGeolocation)
class Geolocation(object):

    def __init__(self, latitude=0, longitude=0):
        self.latitude = float(latitude)
        self.longitude = float(longitude)
