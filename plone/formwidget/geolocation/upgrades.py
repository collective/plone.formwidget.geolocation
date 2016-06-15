# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
import logging


logger = logging.getLogger('plone.formwidget.geolocation upgrade')
PROFILE_ID = 'profile-plone.formwidget.geolocation:default'


def unregister_resource(registry, resource):
    if registry and registry.getResource(resource):
        registry.unregisterResource(resource)
        logger.info("Removed {0} from {1}".format(resource, registry.id))


def upgrade_1_to_2(context):
    """Remove JS and CSS resources from portal_css and portal_js registry.
    Import resource registry configuration.
    """

    # Unregister JavaScript
    unregister_resource(
        getToolByName(context, 'portal_javascripts'),
        '++resource++plone.formwidget.geolocation/libs.js'
    )
    unregister_resource(
        getToolByName(context, 'portal_javascripts'),
        '++resource++plone.formwidget.geolocation/maps.js'
    )

    # Unregister CSS
    unregister_resource(
        getToolByName(context, 'portal_css'),
        '++resource++plone.formwidget.geolocation/libs.css'
    )
    unregister_resource(
        getToolByName(context, 'portal_css'),
        '++resource++plone.formwidget.geolocation/maps.css'
        '++resource++collective.venue/styles.css'
    )

    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'plone.app.registry')
