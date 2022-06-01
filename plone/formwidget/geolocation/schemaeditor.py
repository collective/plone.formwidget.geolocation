# -*- coding: utf-8 -*-
from plone.app.dexterity.browser.types import ALLOWED_FIELDS
from plone.formwidget.geolocation import GeolocationField
from plone.formwidget.geolocation.interfaces import GeolocationMessageFactory as _
try:
    from plone.schemaeditor.fields import FieldFactory
    GeolocationFactory = FieldFactory(GeolocationField, _(u'label_map_field', default=u'Map'))
except ImportError:
    pass

allowedFields = ALLOWED_FIELDS + [u'plone.formwidget.geolocation.GeolocationFactory']
