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
        geosearch,
        map_wrap;

    map_wrap = $(el).closest('div.geolocation_wrapper');
    editable = map_wrap.hasClass('edit');

    var update_inputs = function(lat, lng) {
      map_wrap.find('input.latitude').attr('value', lat);
      map_wrap.find('input.longitude').attr('value', lng);
    };

    var bind_draggable_marker = function (marker) {
      marker.on('dragend', function(e) {
        var coords = e.target.getLatLng();
        update_inputs(coords.lat, coords.lng);
      });
    };

    var create_markers = function (geopoints, editable) {
        // return MarkerClusterGroup from geopoints
        // geopoints = [{lat: NUMBER, lng: NUMBER, popup: STRING}]
        var markers = new L.MarkerClusterGroup();
        for(var i = 0, size = geopoints.length; i < size ; i++){
          var geopoint = geopoints[i],
              marker;
          marker = new L.Marker([geopoint.lat, geopoint.lng], {
            icon: green_marker,
            draggable: editable
          });
          if (geopoint.popup) {
            marker.bindPopup(geopoint.popup);
          }
          if (editable) {
            bind_draggable_marker(marker);
          }
          markers.addLayer(marker);
        }
        return markers;
    };

    // MAP INIT
    map = new L.Map(el, {
      fullscreenControl: true
    });

    L.Icon.Default.imagePath = '++resource++plone.formwidget.geolocation/images';

    // Layers
    baseLayers = {
      'Map': L.tileLayer.provider('OpenStreetMap.Mapnik'),
      'Satellite': L.tileLayer.provider('Esri.WorldImagery'),
      'Topographic': L.tileLayer.provider('OpenTopoMap'),
      'Toner': L.tileLayer.provider('Stamen.Toner'),
    };
    baseLayers['Map'].addTo(map);
    L.control.layers(baseLayers).addTo(map);

    // Awesome Marker
    var green_marker = L.AwesomeMarkers.icon({
      markerColor: 'green'
    });

    // ADD MARKERS
    var geopoints = $(el).data().geopoints;
    var markers = create_markers(geopoints, editable);
    map.addLayer(markers);

    // autozoom
    bounds = markers.getBounds();
    map.fitBounds(bounds);

    if (editable) {
      map.on('geosearch_showlocation', function(e) {
        map.removeLayer(markers);
        var coords = e.Location;
        update_inputs(coords.Y, coords.X);
        bind_draggable_marker(e.Marker);
      });

      // GEOSEARCH
      geosearch = new L.Control.GeoSearch({
        showMarker: true,
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
