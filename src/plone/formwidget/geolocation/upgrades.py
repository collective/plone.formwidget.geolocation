from plone import api
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import IResourceRegistry
from zope.component import getUtility

import logging


logger = logging.getLogger("plone.formwidget.geolocation upgrade")
PROFILE_ID = "profile-plone.formwidget.geolocation:default"


def unregister_resource(registry, resource):
    if registry and registry.getResource(resource):
        registry.unregisterResource(resource)
        logger.info(f"Removed {resource} from {registry.id}")


def upgrade_1_to_2(context):
    """Remove JS and CSS resources from portal_css and portal_js registry.
    Import resource registry configuration.
    """

    # Unregister JavaScript
    unregister_resource(
        getToolByName(context, "portal_javascripts"),
        "++resource++plone.formwidget.geolocation/libs.js",
    )
    unregister_resource(
        getToolByName(context, "portal_javascripts"),
        "++resource++plone.formwidget.geolocation/maps.js",
    )

    # Unregister CSS
    unregister_resource(
        getToolByName(context, "portal_css"),
        "++resource++plone.formwidget.geolocation/libs.css",
    )
    unregister_resource(
        getToolByName(context, "portal_css"),
        "++resource++plone.formwidget.geolocation/maps.css"
        "++resource++collective.venue/styles.css",
    )

    setup = getToolByName(context, "portal_setup")
    setup.runImportStepFromProfile(PROFILE_ID, "plone.app.registry")


def upgrade_2_to_3(context):
    """Remove unused bundles and resources."""

    registry = getUtility(IRegistry)
    records = registry.collectionOfInterface(
        IResourceRegistry, prefix="plone.resources", check=False
    )
    if "geolocation-bundle-resource" in records:
        del records["geolocation-bundle-resource"]

    records = registry.collectionOfInterface(
        IResourceRegistry, prefix="plone.bundles", check=False
    )
    if "geolocation-bundle" in records:
        del records["geolocation-bundle"]

    setup = getToolByName(context, "portal_setup")
    setup.runAllImportStepsFromProfile("profile-plone.patternslib:default")


def upgrade_4_to_5(context):
    context.runImportStepFromProfile(
        "profile-plone.formwidget.geolocation:default", "plone.app.registry"
    )
    api.portal.set_registry_record("geolocation.default_latitude", 0.0)
    api.portal.set_registry_record("geolocation.default_longitude", 0.0)


def upgrade_5_to_6(context):
    context.runImportStepFromProfile(
        "profile-plone.formwidget.geolocation:default", "plone.app.registry"
    )
