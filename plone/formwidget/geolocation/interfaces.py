from z3c.form.interfaces import IWidget
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.schema.interfaces import IObject
from plone.formwidget.geolocation import bounds


_ = MessageFactory('plone.formwidget.geolocation')


class IGeolocation(Interface):
    latitude = schema.Float(title=_(u'Latitude'))
    longitude = schema.Float(title=_(u'Longitude'))
    bounds = bounds.BoundsField(title=_(u'Bounds'))


class IGeolocationField(IObject):
    pass


class IGeolocationWidget(IWidget):
    pass
