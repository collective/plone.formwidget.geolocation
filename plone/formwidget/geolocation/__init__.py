from zope.i18nmessageid import MessageFactory
_ = MessageFactory('plone.formwidget.geolocation')

from plone.formwidget.geolocation.geolocation import Geolocation
from plone.formwidget.geolocation.field import GeolocationField

__all__ = (_, Geolocation, GeolocationField)