try:
    from plone.supermodel.exportimport import BaseHandler
    from plone.formwidget.geolocation.field import GeolocationField
    GeolocationHandler = BaseHandler(GeolocationField)
except ImportError:
    pass
