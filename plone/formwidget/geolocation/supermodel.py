# -*- coding: utf-8 -*-
try:
    from plone.formwidget.geolocation.field import GeolocationField
    from plone.supermodel.exportimport import BaseHandler
    GeolocationHandler = BaseHandler(GeolocationField)
except ImportError:
    pass
