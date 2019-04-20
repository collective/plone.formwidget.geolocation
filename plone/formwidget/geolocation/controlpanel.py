# -*- coding: utf-8 -*-
from plone.formwidget.geolocation.interfaces import IGeolocationSettings
from plone.app.registry.browser import controlpanel


class GeolocationControlPanelForm(controlpanel.RegistryEditForm):

    id = "GeolocationControlPanel"
    schema = IGeolocationSettings
    schema_prefix = "geolocation"

    label = u"Geolocation Settings"
    description = "Settings for Maps and API Keys."


class GeolocationControlPanel(controlpanel.ControlPanelFormWrapper):
    form = GeolocationControlPanelForm
