============================
Geolocation field and widget
============================

.. image:: https://github.com/collective/plone.formwidget.geolocation/actions/workflows/plone-package-test.yml/badge.svg
    :target: https://github.com/collective/plone.formwidget.geolocation/actions/workflows/plone-package-test.yml
    :alt: CI Status


This package provides a z3c.form field and a widget implementing LeafletJS
from plone.patternslib to define Latitude / Longitude informations.

This package is used as a dependency in some other Plone add-ons, like
`collective.geolocationbehavior <https://github.com/collective/collective.geolocationbehavior>`_
but can also be used directly in your own content type schema::

    from plone.formwidget.geolocation import GeolocationField

    ...

    geolocation = GeolocationField(
        title="Geolocation",
        description="Select the location of this content",
    )


Limitations
-----------

This add-on has been developed on Plone 4.3, but works with Plone 5 and Plone 6 too.
Current branch is tested on Plone 5.2.x & Plone 6.0.x.


Translations
------------

This product has been translated into

- French


Contribute
----------

- Issue Tracker: https://github.com/collective/plone.formwidget.geolocation/issues
- Source Code: https://github.com/collective/plone.formwidget.geolocation


License
-------

The project is licensed under the GPLv2.
