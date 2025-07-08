============================
Geolocation field and widget
============================

.. image:: https://github.com/collective/plone.formwidget.geolocation/actions/workflows/plone-package-test.yml/badge.svg
    :target: https://github.com/collective/plone.formwidget.geolocation/actions/workflows/plone-package-test.yml
    :alt: CI Status


This package provides a z3c.form field and a widget implementing `LeafletJS <https://leafletjs.com/>`_
from `pat-leaflet` to define Latitude / Longitude information.


Features
========

- ``GeolocationField`` field included to use in your project.
- ``Geolocation`` control panel included to define the Maps parameters.


Screenshots
===========

After installation, you will find a new behavior available, go to ``Site Setup`` > ``Add-on Configuration`` > ``Geolocation`` as the following screenshot:

.. figure:: https://raw.githubusercontent.com/collective/plone.formwidget.geolocation/refs/heads/master/docs/images/geolocation-controlpanel.png
   :align: center
   :height: 935px
   :width: 799px
   :alt: The Geolocation Settings

   The Geolocation Settings.


Use
===

This package is used as a dependency in some other Plone add-ons, like
`collective.geolocationbehavior <https://github.com/collective/collective.geolocationbehavior>`_
but can also be used directly in your own content type schema:

::

    from plone.formwidget.geolocation import GeolocationField

    ...

    geolocation = GeolocationField(
        title="Geolocation",
        description="Select the location of this content",
    )

The map marker has a popup containing object title / description (by default).
The template and/or the class used to generate the popup content can be overridden
to change it (see ``@@geolocation-geojson-popup`` view).


Versions
========

- plone.formwidget.geolocation 3.0.x -> Plone 6.0.x
- plone.formwidget.geolocation 2.2.x -> Plone 5.2.x


Examples
========

This add-on can be seen in action at the following add-ons:

- https://github.com/collective/collective.collectionfilter
- https://github.com/collective/collective.contentsections
- https://github.com/collective/collective.venue
- https://github.com/collective/Products.Maps
- https://github.com/collective/collective.maplocbehavior


Translations
============

This product has been translated into

- Dutch
- French
- German
- Spanish


Installation
============

Add the ``plone.formwidget.geolocation`` into the file ``backend/pyproject.toml`` in the section ``dependencies``.

::

    dependencies = [
        "Products.CMFPlone==6.1.2",
        "plone.api",
        "plone.restapi",
        "plone.volto",
        "plone.formwidget.geolocation",
    ]

and then running "make backend-build".


Contribute
==========

- Issue Tracker: https://github.com/collective/plone.formwidget.geolocation/issues
- Source Code: https://github.com/collective/plone.formwidget.geolocation


Support
=======

If you are having issues, please let us know at our `issue tracker <https://github.com/collective/plone.formwidget.geolocation/issues>`_.


License
=======

The project is licensed under the GPLv2.
