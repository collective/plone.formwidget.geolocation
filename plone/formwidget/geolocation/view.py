# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView


class MapsConfiguration(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def default_location(self):
        key_lat = "geolocation.default_latitude"
        key_lon = "geolocation.default_longitude"
        lat = api.portal.get_registry_record(key_lat, default=0.0)
        lon = api.portal.get_registry_record(key_lon, default=0.0)
        return (lat, lon)
