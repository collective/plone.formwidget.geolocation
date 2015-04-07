/* jslint browser: true */
/* global jQuery, L */

(function($) {
  "use strict";

  var _initialize_map = function (el) {
    // Initialize the map
    var editable,
        map,
        baseLayers,
        markers,
        bounds,
        update_inputs,
        geosearch,
        geopoints,
        map_wrap;

    map_wrap = $(el).closest('div.geolocation_wrapper');
    editable = map_wrap.hasClass('edit');

    map = new L.Map(el, {
      fullscreenControl: true
    });

    // Layers
    baseLayers = {
      'Map': L.tileLayer.provider('OpenStreetMap.HOT'),
      'Satellite': L.tileLayer.provider('Esri.WorldImagery'),
      'Outdoors': L.tileLayer.provider('Thunderforest.Outdoors'),
      'Toner': L.tileLayer.provider('Stamen.Toner'),
    };
    baseLayers['Map'].addTo(map);
    L.control.layers(baseLayers).addTo(map);

    // Awesome Marker
    var green_marker = L.AwesomeMarkers.icon({
      markerColor: 'green'
    });

    // ADD MARKERS
    markers = new L.MarkerClusterGroup();
    geopoints = $(el).data().geopoints;
    for(var i = 0, size = geopoints.length; i < size ; i++){
      var geopoint = geopoints[i],
          marker;
      marker = new L.Marker([geopoint.lat, geopoint.lng], {
        icon: green_marker,
        draggable: editable
      });
      marker.bindPopup(geopoint.popup);
      if (editable) {
        marker.on('dragend', function(e) {
          var coords = e.target.getLatLng();
          update_inputs(coords.lat, coords.lng);
        });
      }
      markers.addLayer(marker);
    }
    map.addLayer(markers);

    // autozoom
    bounds = markers.getBounds();
    map.fitBounds(bounds);

    update_inputs = function(lat, lng) {
      map_wrap.find('input.latitude').attr('value', lat);
      map_wrap.find('input.longitude').attr('value', lng);
    };
    if (editable) {
      map.on('geosearch_showlocation', function(e) {
        var coords = e.Location;
        update_inputs(coords.Y, coords.X);
      });

      // GEOSEARCH
      geosearch = new L.Control.GeoSearch({
        draggable: editable,
        provider: new L.GeoSearch.Provider.Esri()
        //provider: new L.GeoSearch.Provider.Google()
        //provider: new L.GeoSearch.Provider.OpenStreetMap()
      });
      geosearch.addTo(map);
    }

  };

  // keep that here to be reused elsewhere.
  var initialize_map = function () {
    $('.map').each(function () {
      _initialize_map(this);
    });
  };
  window.plone_formwidget_geolocation__initialize_map = initialize_map;

  $(document).ready(function() {
    initialize_map();
  });

}(jQuery));
