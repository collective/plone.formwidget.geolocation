# -*- coding: utf-8 -*-

from zope.i18nmessageid import MessageFactory


_ = MessageFactory("plone.formwidget.geolocation")

from plone.formwidget.geolocation.field import GeolocationField  # noqa
from plone.formwidget.geolocation.geolocation import Geolocation  # noqa


__all__ = ("Geolocation", "GeolocationField")
