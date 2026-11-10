from plone.formwidget.geolocation import _
from zope.globalrequest import getRequest
from zope.i18n import translate
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

default_map_layer = "OpenStreetMap.Mapnik"
default_map_layers = [
    "OpenStreetMap.Mapnik",
    "Esri.WorldImagery",
    "CartoDB.DarkMatter",
]


@provider(IVocabularyFactory)
def MapLayers(context):
    """Vocabulary for available Leaflet map layers.
    Every value must be a provider (variant) of the leaflet-providers
    version in the bundle (4.0.0), otherwise the map does not render.
    For a full list, see:
    http://leaflet-extras.github.io/leaflet-providers/preview/
    """
    request = getRequest()
    items = [
        (
            _("OpenStreetMap.Mapnik", default="OpenStreetMap Mapnik"),
            "OpenStreetMap.Mapnik",
        ),
        (_("OpenStreetMap.DE", default="OpenStreetMap DE"), "OpenStreetMap.DE"),
        (
            _("OpenStreetMap.France", default="OpenStreetMap France"),
            "OpenStreetMap.France",
        ),
        (_("OpenTopoMap", default="OpenTopoMap"), "OpenTopoMap"),
        (_("BasemapAT.basemap", default="basemap.at"), "BasemapAT.basemap"),
        (_("BasemapAT.grau", default="basemap.at Gray"), "BasemapAT.grau"),
        (
            _("BasemapAT.orthofoto", default="basemap.at Orthophoto"),
            "BasemapAT.orthofoto",
        ),
        (
            _("Thunderforest.OpenCycleMap", default="Thunderforest Cycle Map"),
            "Thunderforest.OpenCycleMap",
        ),
        (
            _("Thunderforest.Transport", default="Thunderforest Transport"),
            "Thunderforest.Transport",
        ),
        (
            _("Thunderforest.TransportDark", default="Thunderforest Transport Dark"),
            "Thunderforest.TransportDark",
        ),
        (
            _("Thunderforest.Outdoors", default="Thunderforest Outdoors"),
            "Thunderforest.Outdoors",
        ),
        (
            _("Esri.WorldStreetMap", default="Esri World Street Map"),
            "Esri.WorldStreetMap",
        ),
        (
            _("Esri.WorldTopoMap", default="Esri World Topo Map"),
            "Esri.WorldTopoMap",
        ),
        (
            _("Esri.WorldImagery", default="Esri World Imagery"),
            "Esri.WorldImagery",
        ),
        (
            _("Esri.WorldTerrain", default="Esri World Terrain"),
            "Esri.WorldTerrain",
        ),
        (
            _("Esri.WorldShadedRelief", default="Esri World Shaded Relief"),
            "Esri.WorldShadedRelief",
        ),
        (
            _("Esri.WorldPhysical", default="Esri World Physical"),
            "Esri.WorldPhysical",
        ),
        (
            _("Esri.OceanBasemap", default="Esri Ocean Basemap"),
            "Esri.OceanBasemap",
        ),
        (
            _("Esri.NatGeoWorldMap", default="Esri Nat Geo World Map"),
            "Esri.NatGeoWorldMap",
        ),
        (
            _("Esri.WorldGrayCanvas", default="Esri World Gray Canvas"),
            "Esri.WorldGrayCanvas",
        ),
        (_("CartoDB.Positron", default="CartoDB Positron"), "CartoDB.Positron"),
        (
            _("CartoDB.PositronNoLabels", default="CartoDB Positron No Labels"),
            "CartoDB.PositronNoLabels",
        ),
        (_("CartoDB.Voyager", default="CartoDB Voyager"), "CartoDB.Voyager"),
        (
            _("CartoDB.DarkMatter", default="CartoDB Dark Matter"),
            "CartoDB.DarkMatter",
        ),
        (
            _("CartoDB.DarkMatterNoLabels", default="CartoDB Dark Matter No Labels"),
            "CartoDB.DarkMatterNoLabels",
        ),
        (
            _("NASAGIBS.ViirsEarthAtNight2012", default="NASA Earth at Night 2012"),
            "NASAGIBS.ViirsEarthAtNight2012",
        ),
    ]
    items = [
        SimpleTerm(title=translate(i[0], context=request), value=i[1]) for i in items
    ]
    return SimpleVocabulary(items)


def valid_map_layers(layers, default=None):
    """Drop stored layers that are no longer offered.

    A layer id unknown to leaflet-providers makes pat-leaflet fail and the map
    stays empty, so settings saved before a provider was removed from the
    vocabulary must not reach the map configuration.

    Returns the still available layers and a usable default layer.
    """
    available = {term.value for term in MapLayers(None)}
    layers = [layer for layer in layers or [] if layer in available]
    if default not in available:
        default = layers[0] if layers else default_map_layer
    return layers, default
