Changelog
=========

2.0 (2016-10-06)
----------------

- Make geolocation formwidget work with ``pat-leaflet``.
  [thet]

- Support for Plone 5 only, using plone.patternslib and providing an own bundle.
  [thet]


1.4 (2015-11-26)
----------------

- Leaflet: After searching, bind new marker to update lat/lng input field and
  remove MarkerClusterGroup. Fix annoying 'Uncaught Error: Couldn't autodetect
  L.Icon.Default.imagePath, set it manually.'
  [thet]

- Update Leaflet dependencies.
  [thet]


1.3 (2015-07-15)
----------------

- Add Leaflet as mapping widget. Use bower/grunt managed resources.
  [thet]

- Remove the ``div.geolocation`` elements. Instead, render the list of
  geolocation points as JSON value on a ``data-geopoints`` attrbute on the map
  element.
  [thet]

- Reintroduce package level imports and avoid circular import by moving out the
  message factory.
  [thet]

- Remove the ``map`` id attrbute on the map element and use instead a ``map``
  css class.
  [thet]


1.2.1 (2015-03-04)
------------------

- Avoid circular imports by removing the package level imports.
  [thet]


1.2 (2015-03-04)
----------------

- PEP8.
  [thet]


1.1 (2014-04-30)
----------------

- Simplify templates and cleanup Google Map leftovers.
  [thet]

- Convert default locations strings from Products.Maps to tuples with floats.
  [thet]

- Improve handling of non-required geolocation fields
  with missing values.
  [davisagli]

- Fix display template markup to be compatible with recent versions
  of Products.Maps.
  [davisagli]

- Add supermodel import/export handler.
  [davisagli]

- Fix declaration of exported names.
  [davisagli]

- Remove dependency on Products.Maps. Don't fail, if default_location is not
  set or maps_configuration adapter not found.
  [thet]


1.0 (2013-02-07)
----------------

- Initial release
