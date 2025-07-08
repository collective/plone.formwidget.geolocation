from zope.i18nmessageid import MessageFactory


PACKAGE_NAME = "plone.formwidget.geolocation"

_ = MessageFactory(PACKAGE_NAME)

from plone.formwidget.geolocation.field import GeolocationField  # noqa
from plone.formwidget.geolocation.geolocation import Geolocation  # noqa


__all__ = ("Geolocation", "GeolocationField")
