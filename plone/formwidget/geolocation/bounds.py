from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.schema.interfaces import IObject
from zope.interface import implements
from zope.interface import Interface


_ = MessageFactory('plone.formwidget.geolocation')


class IBounds(Interface):
    south = schema.Float(title=_(u'South'))
    west = schema.Float(title=_(u'West'))
    north = schema.Float(title=_(u'North'))
    east = schema.Float(title=_(u'East'))


class Bounds(object):
    implements(IBounds)

    def __init__(self, south=0, west=0, north=0, east=0):
        self.south = float(south)
        self.west = float(west)
        self.north = float(north)
        self.east = float(east)


class IBoundsField(IObject):
    pass


class BoundsField(schema.Object):
    implements(IBoundsField)

    _type = Bounds
    schema = IBounds

    def __init__(self, **kw):
        super(BoundsField, self).__init__(schema=self.schema, **kw)
