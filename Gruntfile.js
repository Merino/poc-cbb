module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    //uglify: {
    //  options: {
    //    banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
    //  },
    //  build: {
    //    src: 'panels/source/apps/javascript/demo.js',
    //    dest: 'panels/static/javascript/panels.js'
    //  }
    //},

    sass: {
        dist: {
          options: {
            style: 'expanded'
          },
          files: {                         // Dictionary of files
            'vesper/static/vds/apps/css/apps.css': 'vds/source/apps/css/apps.scss',
            'vesper/static/vds/apps/css/libs.css': 'vds/source/vendors/libs.scss'
          }
        }
    },

    concat: {
        dist: {
            files: {
                'vesper/static/vds/apps/javascript/apps.js': [
                    'vds/source/apps/javascript/_apps.js'
                    ],
                'vesper/static/vds/apps/javascript/libs.js': [
                    'vds/source/vendors/jquery/jquery-3.1.1.min.js',
                    'vds/source/vendors/django-1.9/javascript/inlines.js',
                    //'panels/source/vendors/bootstrap/assets/javascripts/bootstrap.min.js',
                    //'panels/source/vendors/turbolinks/turbolinks.js'
                    ],
            },
        }
    },

    watch: {
        css: {
            files: 'vds/source/**/*.scss',
            tasks: ['sass:dist', 'postcss'],
        }
    },

    postcss: {
        options: {
          map: true, // inline sourcemaps

          // or
          //map: {
          //    inline: false, // save all sourcemaps as separate files...
          //    annotation: 'dist/css/maps/' // ...to the specified directory
          //},

          processors: [
            require('postcss-slds-prefix')('vds'), // add fallbacks for rem units
          ]
        },
        dist: {
          src: 'vesper/static/vds/apps/css/*.css'
        }
    },

    copy: {
        fonts: {
            expand: true,
            cwd: '.',
            src: [
                'vds/source/vendors/font-awesome-4.7.0/fonts/*'],
            dest: 'vesper/static/vds/apps/fonts/',
            filter: 'isFile',
            flatten: true
        },
        image: {
            expand: true,
            cwd: '.',
            src: [
                'vds/source/apps/image/*',
            ],
            dest: 'vesper/static/vds/apps/image/',
            filter: 'isFile',
            flatten: true
        },
        tinymce: {
            expand: true,
            cwd: 'vds/source/vendors/tinymce-4.4.3/js/tinymce/',
            src: [
                '**',
            ],
            dest: 'vesper/static/vds/libs/tinymce/',
        }
    }
  });

  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-postcss');

  // Default task(s).
  grunt.registerTask('default', ['watch']);
  grunt.registerTask('build', ['sass', 'postcss', 'copy', 'concat']);
};