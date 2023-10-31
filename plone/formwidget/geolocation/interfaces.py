from plone.formwidget.geolocation import _
from plone.formwidget.geolocation.vocabularies import default_map_layer
from plone.formwidget.geolocation.vocabularies import default_map_layers
from z3c.form.interfaces import IWidget
from zope import schema
from zope.interface import Interface
from zope.schema.interfaces import IObject


class IGeolocation(Interface):
    latitude = schema.Float(title=_("Latitude"), required=False)
    longitude = schema.Float(title=_("Longitude"), required=False)


class IGeolocationField(IObject):
    pass


class IGeolocationWidget(IWidget):
    pass


class IGeolocationSettings(Interface):
    fullscreen_control = schema.Bool(
        title=_("label_maps_fullscreen", default="Show Fullscreen Control"),
        required=False,
        default=True,
    )

    locate_control = schema.Bool(
        title=_("label_maps_locate", default="Show Locate Control"),
        required=False,
        default=True,
    )

    zoom_control = schema.Bool(
        title=_("label_maps_zoom", default="Show Zoom Control"),
        required=False,
        default=True,
    )

    show_minimap = schema.Bool(
        title=_("label_maps_show_minimap", default="Show Minimap"),
        required=False,
        default=True,
    )

    show_geosearch = schema.Bool(
        title=_("label_maps_show_geosearch", default="Show Geosearch"),
        required=False,
        default=True,
    )

    show_add_marker = schema.Bool(
        title=_("label_maps_show_add_marker", default="Show Add Marker"),
        required=False,
        default=False,
    )

    geosearch_provider = schema.TextLine(
        title=_("label_maps_geosearch_provider", default="Geosearch Provider"),
        required=False,
        default="nominatim",
    )

    google_api_key = schema.TextLine(
        title=_("label_google_api_key", default="Google maps API Key"),
        description=_(
            "help_google_api_key",
            default="If you want to use the Google Maps search API for higher accuracy, you have to provide a Google Maps API key here.",
        ),
        required=False,
        default=None,
    )

    show_google_maps_link = schema.Bool(
        title=_("label_google_maps_link", default="Show Google maps link"),
        description=_(
            "help_google_maps_link",
            default="Show a link to the Google Maps site, which can be used for further actions like routing.",
        ),
        required=False,
        default=False,
    )

    default_map_layer = schema.Choice(
        title=_("default_map_layer", "Default map layer"),
        description=_("help_default_map_layer", default="Set the default map layer"),
        required=False,
        default=default_map_layer,
        vocabulary="plone.formwidget.geolocation.vocabularies.map_layers",
    )

    map_layers = schema.List(
        title=_("label_map_layers", "Map Layers"),
        description=_("help_map_layers", default="Set the available map layers"),
        required=False,
        default=default_map_layers,
        missing_value=[],
        value_type=schema.Choice(
            vocabulary="plone.formwidget.geolocation.vocabularies.map_layers"
        ),
    )

    default_latitude = schema.Float(
        title=_("Default latitude"),
        description=_(
            "Latitude value that will be used to center map (on contents not yet geolocated)."
        ),
        required=False,
    )

    default_longitude = schema.Float(
        title=_("Default longitude"),
        description=_(
            "Longitude value that will be used to center map (on contents not yet geolocated)."
        ),
        required=False,
    )

    use_default_geolocation_as_value = schema.Bool(
        title=_("Use default geolocation for contents"),
        description=_(
            "Geolocation used to center map (see above) will also be used to define the default geolocation on new contents."
        ),
        required=False,
        default=True,
    )

    default_input_zoom = schema.Int(
        title=_("Default zoom (edit)"),
        description=_("Default zoom for geolocation widget in edit mode"),
        required=False,
        default=14,
    )

    default_display_zoom = schema.Int(
        title=_("Default zoom (view)"),
        description=_("Default zoom for geolocation widget in view mode"),
        required=False,
        default=14,
    )
