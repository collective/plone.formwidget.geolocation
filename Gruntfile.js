/* global module */
module.exports = function(grunt) {
  "use strict";

  var dest_path = 'plone/formwidget/geolocation/resources/';

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    concat: {
      options: {
        separator: grunt.util.linefeed + grunt.util.linefeed
      },
      js: {
        src: [
          'bower_components/leaflet/dist/leaflet-src.js',
          'bower_components/Leaflet.fullscreen/dist/Leaflet.fullscreen.js',
          'bower_components/leaflet-providers/leaflet-providers.js',
          'bower_components/L.GeoSearch/src/js/l.control.geosearch.js',
          'bower_components/L.GeoSearch/src/js/l.geosearch.provider.esri.js',
          'bower_components/leaflet.markercluster/dist/leaflet.markercluster-src.js',
          'bower_components/Leaflet.awesome-markers/dist/leaflet.awesome-markers.js'
        ],
        dest: dest_path + 'libs.js'
      },
      css: {
        src: [
          'bower_components/leaflet/dist/leaflet.css',
          'bower_components/Leaflet.fullscreen/dist/leaflet.fullscreen.css',
          'bower_components/L.GeoSearch/src/css/l.geosearch.css',
          'bower_components/leaflet.markercluster/dist/MarkerCluster.Default.css',
          'bower_components/leaflet.markercluster/dist/MarkerCluster.css',
          'bower_components/Leaflet.awesome-markers/dist/leaflet.awesome-markers.css'
        ],
        dest: dest_path + 'libs.css'
      }
    },

    uglify: {
      default: {
        options: {
          sourceMap: true,
          sourceMapName: dest_path + 'libs.min.js.map',
          sourceMapIncludeSources: false
        },
        files: {
          'plone/formwidget/geolocation/resources/libs.min.js': [dest_path + 'libs.js']
        }
      }
    },

    copy: {
      main: {
        files: [
          {
            expand: true,
            cwd: 'bower_components/leaflet/dist/images/',
            src: ['**'],
            dest: dest_path + 'images/'
          },
          {
            expand: true,
            cwd: 'bower_components/Leaflet.fullscreen/dist/',
            src: ['*.png'],
            dest: dest_path + 'images/'
          },
          {
            expand: true,
            cwd: 'bower_components/Leaflet.awesome-markers/dist/images/',
            src: ['*.png'],
            dest: dest_path + 'images/'
          }
        ]
      }
    },

    sed: {
      'leaflet': {
        path: dest_path + 'libs.css',
        pattern: 'images/',
        replacement: '++resource++plone.formwidget.geolocation/images/'
      },
      'leaflet-fullscreen-1': {
        path: dest_path + 'libs.css',
        pattern: 'fullscreen.png',
        replacement: '++resource++plone.formwidget.geolocation/images/fullscreen.png'
      },
      'leaflet-fullscreen-2': {
        path: dest_path + 'libs.css',
        pattern: 'fullscreen@2x.png',
        replacement: '++resource++plone.formwidget.geolocation/images/fullscreen@2x.png'
      },
    }

  });

  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-sed');

  // Default task(s).
  grunt.registerTask('default', ['concat', 'uglify', 'copy', 'sed']);

};
