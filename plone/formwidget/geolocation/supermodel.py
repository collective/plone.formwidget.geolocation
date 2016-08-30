# -*- coding: utf-8 -*-
from plone.formwidget.geolocation.field import GeolocationField
try:
    from plone.supermodel.exportimport import BaseHandler
    GeolocationHandler = BaseHandler(GeolocationField)
except ImportError:
    pass
