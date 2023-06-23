from plone.api.portal import get_registry_record as getrec
from plone.formwidget.geolocation.interfaces import IGeolocationField
from plone.formwidget.geolocation.interfaces import IGeolocationWidget
from plone.formwidget.geolocation.vocabularies import _
from z3c.form.browser.text import TextWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.component import queryMultiAdapter
from zope.i18n import translate
from zope.interface import implementer
from zope.interface import implementer_only

import json


@implementer_only(IGeolocationWidget)
class GeolocationWidget(TextWidget):
    klass = "geolocation-widget"
    value = None

    def update(self):
        super().update()
        self.coordinates = self.value
        if self.coordinates is None or not all(self.coordinates):
            # determine default location from settings if the context
            self.update_default_location()

    @property
    def id_input_lat(self):
        return f"{self.id}_latitude"

    @property
    def id_input_lng(self):
        return f"{self.id}_longitude"

    @property
    def data_geojson(self):
        """Return the geo location as GeoJSON string."""
        if not self.coordinates or not all(self.coordinates):
            return

        popup_view = queryMultiAdapter(
            (self.context, self.request), name="geolocation-geojson-popup"
        )
        geo_json = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        "popup": popup_view(),
                        "main": True,
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            self.coordinates[1],  # longitude
                            self.coordinates[0],  # latitude
                        ],
                    },
                },
            ],
        }

        if self.mode == "input":
            properties = geo_json["features"][0]["properties"]
            properties["editable"] = True
            properties["no_delete"] = True
            properties["latinput"] = f"#{self.id_input_lat}"
            properties["lnginput"] = f"#{self.id_input_lng}"

        return json.dumps(geo_json)

    @property
    def map_configuration(self):
        map_layers = getrec("geolocation.map_layers") or []
        config = {
            "fullscreencontrol": getrec("geolocation.fullscreen_control"),
            "locatecontrol": getrec("geolocation.locate_control"),
            "zoomcontrol": getrec("geolocation.zoom_control"),
            "minimap": getrec("geolocation.show_minimap"),
            "addmarker": getrec("geolocation.show_add_marker"),
            "geosearch": getrec("geolocation.show_geosearch"),
            "geosearch_provider": getrec("geolocation.geosearch_provider"),
            "default_map_layer": getrec("geolocation.default_map_layer"),
            "map_layers": [
                {
                    "title": translate(_(layer), context=self.request),
                    "id": layer,
                }
                for layer in map_layers
            ],
            "latitude": self.coordinates[0],
            "longitude": self.coordinates[1],
        }

        if self.mode == "input":
            # geosearch for input is always active
            config["geosearch"] = True
            # zoomcontrol for input is always active
            config["zoomcontrol"] = True

        return json.dumps(config)

    def update_default_location(self):
        if getrec("geolocation.use_default_geolocation_as_value"):
            # we want to inject default values when creating a content
            # the values are injected to self.value (input fields)
            # and self.coordinates (map marker)
            self.value = self.coordinates = (
                getrec("geolocation.default_latitude"),
                getrec("geolocation.default_longitude")
            )

        if self.coordinates is None or not all(self.coordinates):
            # no default value for contents not yet geolocated
            # the display template will not show the map at all
            # NOTE: when creating a content, self.value is None so we have to
            # set the initial lat/lng tuple here
            self.value = (None, None)
            if self.mode == "input":
                # fallback to ("0", "0") for input mode to show the map and the marker
                self.coordinates = ("0", "0")


@implementer(IFieldWidget)
@adapter(IGeolocationField, IFormLayer)
def GeolocationFieldWidget(field, request):
    return FieldWidget(field, GeolocationWidget(request))
