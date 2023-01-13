Changelog
=========

3.0.4 (unreleased)
------------------

- Nothing changed yet.


3.0.3 (2023-01-13)
------------------

- Fix configlet: boolean field cannot be required (otherwise it is impossible
  to set it to False)
  [laulaz]


3.0.2 (2022-11-10)
------------------

- Fix widget display mode: initialize map with actually saved lat/lon values.
  [petschki]


3.0.1 (2022-10-19)
------------------

- Remove the height style from the geolocation input widget map.
  It is already set by pat-leaflet.
  [thet]


3.0.0 (2022-10-11)
------------------

- Update to ES6 refactored `@patternslib/pat-leaflet`.
- Integrate Plone resources with module federation.
  [petschki]


2.2.5 (2022-09-22)
------------------

- Fix an issue when the geolocation is empty
  [mpeeters, laulaz]

- Allow to change map marker popup default content (#35).
  See ``@@geolocation-geojson-popup`` view.
  [laulaz]


2.2.4 (2022-06-02)
------------------

- Add French translations
  [laulaz]

- Add plone.restapi deserializer (if plone.restapi is installed).
  [laulaz]

- Allow to set default geolocation on new contents (via bool field in config).
  If not checked, the defaut geolocation is only used to center map.
  Also, the geolocation map will not show on an object if no geolocation was defined.
  [laulaz]


2.2.3 (2021-05-26)
------------------

- Add plone.restapi serializer (if plone.restapi is installed).
  [bsuttor, laulaz]

- Specify that latitude and longitude fields can be not required.
  [boulch]

- Allow empty latitude and longitude.
  [bsuttor]


2.2.2 (2020-07-10)
------------------

- Fix popup displaying the string "None" when no description was given.
  [parruc]

- Add default_location informations to maps-configuration view.
  [bsuttor]


2.2.1 (2019-06-07)
------------------

- Translate map ids.
  [thet]


2.2.0 (2019-04-24)
------------------

- add geolocation settings for leaflet
  [petschki]

- Fix for Python 3.
  [pbauer]


2.1.3 (2017-12-06)
------------------

- Only include the leaflet bundle where it is needed via ``add_bundle_on_request``.
  [thet]


2.1.2 (2017-04-04)
------------------

- Explicitly include necessary zcml dependencies to avoid having to explictly doing that in tests.
  plone.app.testing disables z3c.autoinclude.
  [thet]


2.1.1 (2017-03-06)
------------------

- Add upgrade step for changes in 2.1 + register missing upgrade steps for Plone 5 migration.
  [thet]


2.1 (2017-02-28)
----------------

- Use ``bundle-leaflet`` from the ``plone.patternslib`` package.
  This should give an out-of-the-box leaflet integration.
  [thet]

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
