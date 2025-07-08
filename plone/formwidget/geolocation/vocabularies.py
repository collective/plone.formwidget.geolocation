from plone.formwidget.geolocation import _
from zope.globalrequest import getRequest
from zope.i18n import translate
from zope.i18nmessageid import MessageFactory
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
    For a full list, see:
    http://leaflet-extras.github.io/leaflet-providers/preview/
    """
    request = getRequest()
    items = [
        (
            _("OpenStreetMap.Mapnik", default="OpenStreetMap Mapnik"),
            "OpenStreetMap.Mapnik",
        ),
        (
            _("OpenStreetMap.BlackAndWhite", default="OpenStreetMap Black & White"),
            "OpenStreetMap.BlackAndWhite",
        ),
        (_("OpenStreetMap.DE", default="OpenStreetMap DE"), "OpenStreetMap.DE"),
        (
            _("OpenStreetMap.France", default="OpenStreetMap France"),
            "OpenStreetMap.France",
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
        (_("Stamen.Toner", default="Stamen Toner"), "Stamen.Toner"),
        (
            _("Stamen.TonerBackground", default="Stamen Toner Background"),
            "Stamen.TonerBackground",
        ),
        (
            _("Stamen.TonerLite", default="Stamen Toner Lite"),
            "Stamen.TonerLite",
        ),
        (
            _("Stamen.Watercolor", default="Stamen Watercolor"),
            "Stamen.Watercolor",
        ),
        (_("Stamen.Terrain", default="Stamen Terrain"), "Stamen.Terrain"),
        (
            _("Stamen.TerrainBackground", default="Stamen Terrain Background"),
            "Stamen.TerrainBackground",
        ),
        (
            _("Stamen.TopOSMRelief", default="Stamen Relief"),
            "Stamen.TopOSMRelief",
        ),
        (
            _("Esri.WorldStreetMap", default="Esri World Street Map"),
            "Esri.WorldStreetMap",
        ),
        (_("Esri.DeLorme", default="Esri DeLorme"), "Esri.DeLorme"),
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
        (
            _("CartoDB.DarkMatter", default="CatoDB Dark Matter"),
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
