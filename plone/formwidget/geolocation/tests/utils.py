from zope.interface import implementer

from plone.dexterity.content import DexterityContent
from plone.formwidget.geolocation import GeolocationField
from plone.supermodel import model


class IDummyGeolocation(model.Schema):
    geolocation = GeolocationField(title="Geolocation")


@implementer(IDummyGeolocation)
class DummyContent(DexterityContent):
    """ """
