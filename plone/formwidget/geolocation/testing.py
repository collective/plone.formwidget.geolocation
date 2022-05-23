# -*- coding: utf-8 -*-
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plone.formwidget.geolocation


class GeolocationLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(name="testing.zcml", package=plone.formwidget.geolocation)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "plone.formwidget.geolocation:default")


GEOLOCATION_FIXTURE = GeolocationLayer()


GEOLOCATION_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GEOLOCATION_FIXTURE,), name="GeolocationLayer:IntegrationTesting"
)


GEOLOCATION_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GEOLOCATION_FIXTURE,), name="GeolocationLayer:FunctionalTesting"
)
