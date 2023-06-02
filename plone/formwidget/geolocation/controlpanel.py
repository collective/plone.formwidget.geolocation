from plone.app.registry.browser import controlpanel
from plone.formwidget.geolocation import _
from plone.formwidget.geolocation.interfaces import IGeolocationSettings


class GeolocationControlPanelForm(controlpanel.RegistryEditForm):
    id = "GeolocationControlPanel"
    schema = IGeolocationSettings
    schema_prefix = "geolocation"

    label = _("Geolocation Settings")
    description = _("Settings for Maps and API Keys.")


class GeolocationControlPanel(controlpanel.ControlPanelFormWrapper):
    form = GeolocationControlPanelForm
