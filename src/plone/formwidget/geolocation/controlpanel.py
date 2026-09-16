from plone.app.registry.browser import controlpanel
from plone.formwidget.geolocation import _
from plone.formwidget.geolocation.interfaces import IGeolocationSettings
from plone.formwidget.geolocation.widget import CoordinateFieldWidget


class GeolocationControlPanelForm(controlpanel.RegistryEditForm):
    id = "GeolocationControlPanel"
    schema = IGeolocationSettings
    schema_prefix = "geolocation"

    label = _("Geolocation Settings")
    description = _("Settings for Maps and API Keys.")

    def updateFields(self):
        super().updateFields()
        # locale independent input, see widget.CoordinateWidget
        for name in ("default_latitude", "default_longitude"):
            self.fields[name].widgetFactory = CoordinateFieldWidget


class GeolocationControlPanel(controlpanel.ControlPanelFormWrapper):
    form = GeolocationControlPanelForm
