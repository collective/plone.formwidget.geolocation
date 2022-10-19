# -*- coding: utf-8 -*-
from plone.api.portal import get_registry_record as getrec
from plone.formwidget.geolocation.interfaces import IGeolocationField
from plone.formwidget.geolocation.interfaces import IGeolocationWidget
from plone.formwidget.geolocation.vocabularies import _
from Products.CMFPlone.resources import add_bundle_on_request
from Products.CMFPlone.utils import get_top_request
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
        super(GeolocationWidget, self).update()
        if self.value is None and self.mode == "input":
            self.value = self._default_loc()

    @property
    def id_input_lat(self):
        return "{0}_latitude".format(self.id)

    @property
    def id_input_lng(self):
        return "{0}_longitude".format(self.id)

    @property
    def data_geojson(self):
        """Return the geo location as GeoJSON string."""
        coordinates = self.value
        if self.mode != "input" and (not coordinates or not all(coordinates)):
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
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [coordinates[1], coordinates[0]],  # lng  # lat
                    },
                },
            ],
        }

        if self.mode == "input":
            properties = geo_json["features"][0]["properties"]
            properties["editable"] = True
            properties["no_delete"] = True
            properties["latinput"] = "#{0}".format(self.id_input_lat)
            properties["lnginput"] = "#{0}".format(self.id_input_lng)
            # set default lat/lng to 0 if None
            if geo_json["features"][0]["geometry"]["coordinates"][0] is None:
                geo_json["features"][0]["geometry"]["coordinates"][0] = "0"
            if geo_json["features"][0]["geometry"]["coordinates"][1] is None:
                geo_json["features"][0]["geometry"]["coordinates"][1] = "0"

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
                {"title": translate(_(layer), context=self.request), "id": layer}
                for layer in map_layers
            ],
            "latitude": self.value[0],
            "longitude": self.value[1],
        }
        if self.mode == "input":
            # geosearch for input is always active
            config["geosearch"] = True
            # zoomcontrol for input is always active
            config["zoomcontrol"] = True
            # set default lat/lng to 0 if None
            if config["latitude"] is None:
                config["latitude"] = "0"
            if config["longitude"] is None:
                config["longitude"] = "0"
        return json.dumps(config)

    def _default_loc(self):
        if getrec("geolocation.use_default_geolocation_as_value"):
            return (
                getrec("geolocation.default_latitude"),
                getrec("geolocation.default_longitude"),
            )
        # no default value for contents not yet geolocated
        return (None, None)


@implementer(IFieldWidget)
@adapter(IGeolocationField, IFormLayer)
def GeolocationFieldWidget(field, request):
    return FieldWidget(field, GeolocationWidget(request))
