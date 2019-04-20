# -*- coding: utf-8 -*-
from zope.globalrequest import getRequest
from zope.i18n import translate
from zope.i18nmessageid import MessageFactory
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


_ = MessageFactory('plone.formwidget.geolocation')
default_map_layer = 'OpenStreetMap.Mapnik'
default_map_layers = [
    'OpenStreetMap.Mapnik',
    'Esri.WorldImagery',
    'CartoDB.DarkMatter',
]


@provider(IVocabularyFactory)
def MapLayers(context):
    """Vocabulary for available Leaflet map layers.
    For a full list, see:
    http://leaflet-extras.github.io/leaflet-providers/preview/
    """
    request = getRequest()
    items = [
        (translate(_('OpenStreetMap.Mapnik'), request),           'OpenStreetMap.Mapnik'),
        (translate(_('OpenStreetMap.BlackAndWhite'), request),    'OpenStreetMap.BlackAndWhite'),
        (translate(_('OpenStreetMap.DE'), request),               'OpenStreetMap.DE'),
        (translate(_('OpenStreetMap.France'), request),           'OpenStreetMap.France'),
        (translate(_('Thunderforest.OpenCycleMap'), request),     'Thunderforest.OpenCycleMap'),
        (translate(_('Thunderforest.Transport'), request),        'Thunderforest.Transport'),
        (translate(_('Thunderforest.TransportDark'), request),    'Thunderforest.TransportDark'),
        (translate(_('Thunderforest.Outdoors'), request),         'Thunderforest.Outdoors'),
        (translate(_('Stamen.Toner'), request),                   'Stamen.Toner'),
        (translate(_('Stamen.TonerBackground'), request),         'Stamen.TonerBackground'),
        (translate(_('Stamen.TonerLite'), request),               'Stamen.TonerLite'),
        (translate(_('Stamen.Watercolor'), request),              'Stamen.Watercolor'),
        (translate(_('Stamen.Terrain'), request),                 'Stamen.Terrain'),
        (translate(_('Stamen.TerrainBackground'), request),       'Stamen.TerrainBackground'),
        (translate(_('Stamen.TopOSMRelief'), request),            'Stamen.TopOSMRelief'),
        (translate(_('Esri.WorldStreetMap'), request),            'Esri.WorldStreetMap'),
        (translate(_('Esri.DeLorme'), request),                   'Esri.DeLorme'),
        (translate(_('Esri.WorldTopoMap'), request),              'Esri.WorldTopoMap'),
        (translate(_('Esri.WorldImagery'), request),              'Esri.WorldImagery'),
        (translate(_('Esri.WorldTerrain'), request),              'Esri.WorldTerrain'),
        (translate(_('Esri.WorldShadedRelief'), request),         'Esri.WorldShadedRelief'),
        (translate(_('Esri.WorldPhysical'), request),             'Esri.WorldPhysical'),
        (translate(_('Esri.OceanBasemap'), request),              'Esri.OceanBasemap'),
        (translate(_('Esri.NatGeoWorldMap'), request),            'Esri.NatGeoWorldMap'),
        (translate(_('Esri.WorldGrayCanvas'), request),           'Esri.WorldGrayCanvas'),
        (translate(_('CartoDB.DarkMatter'), request),             'CartoDB.DarkMatter'),
        (translate(_('CartoDB.DarkMatterNoLabels'), request),     'CartoDB.DarkMatterNoLabels'),
        (translate(_('NASAGIBS.ViirsEarthAtNight2012'), request), 'NASAGIBS.ViirsEarthAtNight2012'),
    ]  # noqa
    items = [SimpleTerm(title=i[0], value=i[1]) for i in items]
    return SimpleVocabulary(items)
