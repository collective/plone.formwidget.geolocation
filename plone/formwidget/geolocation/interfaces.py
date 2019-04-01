# -*- coding: utf-8 -*-
from plone.formwidget.geolocation.vocabularies import default_map_layer
from plone.formwidget.geolocation.vocabularies import default_map_layers
from z3c.form.interfaces import IWidget
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.schema.interfaces import IObject

_ = MessageFactory('plone.formwidget.geolocation')


class IGeolocation(Interface):
    latitude = schema.Float(title=_(u'Latitude'))
    longitude = schema.Float(title=_(u'Longitude'))


class IGeolocationField(IObject):
    pass


class IGeolocationWidget(IWidget):
    pass


class IGeolocationSettings(Interface):

    fullscreen_control = schema.Bool(
        title=_(u'label_maps_fullscreen', default=u"Show Fullscreen Control"),
        required=False,
        default=True,
    )

    locate_control = schema.Bool(
        title=_(u'label_maps_locate', default=u"Show Locate Control"),
        required=False,
        default=True,
    )

    zoom_control = schema.Bool(
        title=_(u'label_maps_zoom', default=u"Show Zoom Control"),
        required=False,
        default=True,
    )

    show_minimap = schema.Bool(
        title=_(u'label_maps_show_minimap', default=u"Show Minimap"),
        required=False,
        default=True,
    )

    show_geosearch = schema.Bool(
        title=_(u'label_maps_show_geosearch', default=u"Show Geosearch"),
        required=False,
        default=True,
    )

    show_add_marker = schema.Bool(
        title=_(u'label_maps_show_add_marker', default=u"Show Add Marker"),
        required=False,
        default=False,
    )

    geosearch_provider = schema.TextLine(
        title=_(u'label_maps_geosearch_provider', default=u"Geosearch Provider"),  # noqa
        required=False,
        default=u'nominatim',
    )

    google_api_key = schema.TextLine(
        title=_(u'label_google_api_key', default=u'Google maps API Key'),
        description=_(u'help_google_api_key', default=u'If you want to use the Google Maps search API for higher accuracy, you have to provide a Google Maps API key here.'),  # noqa
        required=False,
        default=None
    )

    show_google_maps_link = schema.Bool(
        title=_(u'label_google_maps_link', default=u'Show Google maps link.'),
        description=_(u'help_google_maps_link', default=u'Show a link to the Google Maps site, which can be used for further actions like routing.'),  # noqa
        required=False,
        default=False
    )

    default_map_layer = schema.Choice(
        title=_(
            u'default_map_layer',
            u'Default map layer'
        ),
        description=_(
            u'help_default_map_layer',
            default=u'Set the default map layer'
        ),
        required=False,
        default=default_map_layer,
        vocabulary='plone.formwidget.geolocation.vocabularies.map_layers',
    )

    map_layers = schema.List(
        title=_(u'label_map_layers', u'Map Layers'),
        description=_(
            u'help_map_layers',
            default=u'Set the available map layers'),
        required=False,
        default=default_map_layers,
        missing_value=[],
        value_type=schema.Choice(
            vocabulary='plone.formwidget.geolocation.vocabularies.map_layers'))
