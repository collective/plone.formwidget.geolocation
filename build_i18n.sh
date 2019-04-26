#!/bin/sh
I18NDUDE=i18ndude
I18NPATH=./plone/formwidget/geolocation
DOMAIN=plone.formwidget.geolocation
$I18NDUDE rebuild-pot --pot $I18NPATH/locales/$DOMAIN.pot --create $DOMAIN $I18NPATH
$I18NDUDE sync --pot $I18NPATH/locales/$DOMAIN.pot $I18NPATH/locales/*/LC_MESSAGES/$DOMAIN.po
