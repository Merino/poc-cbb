module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      build: {
        src: 'panels/source/apps/javascript/demo.js',
        dest: 'panels/static/javascript/panels.js'
      }
    },

    sass: {
        dist: {
          options: {
            style: 'expanded'
          },
          files: {                         // Dictionary of files
            'panels/static/css/apps.css': 'panels/source/apps/css/apps.scss',
            'panels/static/css/libs.css': 'panels/source/vendors/libs.scss'
          }
        }
    },

    concat: {
        dist: {
            files: {
                'panels/static/javascript/apps.js': [
                    'panels/source/apps/javascript/_navigation.js'
                    ],
                'panels/static/javascript/libs.js': [
                    'panels/source/vendors/jquery/jquery-1.11.3.min.js',
                    'panels/source/vendors/bootstrap/assets/javascripts/bootstrap.min.js',
                    'panels/source/vendors/turbolinks/turbolinks.js'
                    ],
            },
        }
    },

    watch: {
        css: {
            files: 'panels/source/**/*.scss',
            tasks: ['sass:dist'],
        }
    },

    copy: {
        fonts: {
            expand: true,
            cwd: '.',
            src: [
                'panels/source/vendors/bootstrap/dist/fonts/*',
                'panels/source/vendors/font-awesome/fonts/*'],
            dest: 'panels/static/fonts/',
            filter: 'isFile',
            flatten: true
        }
    }
  });

  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Default task(s).
  grunt.registerTask('default', ['watch']);
  grunt.registerTask('build', ['sass', 'copy', 'concat']);
};