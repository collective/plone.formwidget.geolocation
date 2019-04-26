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
        (_('OpenStreetMap.Mapnik',           default='OpenStreetMap Mapnik'),           'OpenStreetMap.Mapnik'),            # noqa
        (_('OpenStreetMap.BlackAndWhite',    default='OpenStreetMap Black & White'),    'OpenStreetMap.BlackAndWhite'),     # noqa
        (_('OpenStreetMap.DE',               default='OpenStreetMap DE'),               'OpenStreetMap.DE'),                # noqa
        (_('OpenStreetMap.France',           default='OpenStreetMap France'),           'OpenStreetMap.France'),            # noqa
        (_('Thunderforest.OpenCycleMap',     default='Thunderforest Cycle Map'),        'Thunderforest.OpenCycleMap'),      # noqa
        (_('Thunderforest.Transport',        default='Thunderforest Transport'),        'Thunderforest.Transport'),         # noqa
        (_('Thunderforest.TransportDark',    default='Thunderforest Transport Dark'),   'Thunderforest.TransportDark'),     # noqa
        (_('Thunderforest.Outdoors',         default='Thunderforest Outdoors'),         'Thunderforest.Outdoors'),          # noqa
        (_('Stamen.Toner',                   default='Stamen Toner'),                   'Stamen.Toner'),                    # noqa
        (_('Stamen.TonerBackground',         default='Stamen Toner Background'),        'Stamen.TonerBackground'),          # noqa
        (_('Stamen.TonerLite',               default='Stamen Toner Lite'),              'Stamen.TonerLite'),                # noqa
        (_('Stamen.Watercolor',              default='Stamen Watercolor'),              'Stamen.Watercolor'),               # noqa
        (_('Stamen.Terrain',                 default='Stamen Terrain'),                 'Stamen.Terrain'),                  # noqa
        (_('Stamen.TerrainBackground',       default='Stamen Terrain Background'),      'Stamen.TerrainBackground'),        # noqa
        (_('Stamen.TopOSMRelief',            default='Stamen Relief'),                  'Stamen.TopOSMRelief'),             # noqa
        (_('Esri.WorldStreetMap',            default='Esri World Street Map'),          'Esri.WorldStreetMap'),             # noqa
        (_('Esri.DeLorme',                   default='Esri DeLorme'),                   'Esri.DeLorme'),                    # noqa
        (_('Esri.WorldTopoMap',              default='Esri World Topo Map'),            'Esri.WorldTopoMap'),               # noqa
        (_('Esri.WorldImagery',              default='Esri World Imagery'),             'Esri.WorldImagery'),               # noqa
        (_('Esri.WorldTerrain',              default='Esri World Terrain'),             'Esri.WorldTerrain'),               # noqa
        (_('Esri.WorldShadedRelief',         default='Esri World Shaded Relief'),       'Esri.WorldShadedRelief'),          # noqa
        (_('Esri.WorldPhysical',             default='Esri World Physical'),            'Esri.WorldPhysical'),              # noqa
        (_('Esri.OceanBasemap',              default='Esri Ocean Basemap'),             'Esri.OceanBasemap'),               # noqa
        (_('Esri.NatGeoWorldMap',            default='Esri Nat Geo World Map'),         'Esri.NatGeoWorldMap'),             # noqa
        (_('Esri.WorldGrayCanvas',           default='Esri World Gray Canvas'),         'Esri.WorldGrayCanvas'),            # noqa
        (_('CartoDB.DarkMatter',             default='CatoDB Dark Matter'),             'CartoDB.DarkMatter'),              # noqa
        (_('CartoDB.DarkMatterNoLabels',     default='CartoDB Dark Matter No Labels'),  'CartoDB.DarkMatterNoLabels'),      # noqa
        (_('NASAGIBS.ViirsEarthAtNight2012', default='NASA Earth at Night 2012'),       'NASAGIBS.ViirsEarthAtNight2012'),  # noqa
    ]
    items = [
        SimpleTerm(title=translate(i[0], context=request), value=i[1])
        for i in items]
    return SimpleVocabulary(items)
