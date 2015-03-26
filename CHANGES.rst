Changelog
=========

1.3 (unreleased)
----------------

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
