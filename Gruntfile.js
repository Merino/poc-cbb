module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      build: {
        src: 'panels/source/app/javascript/demo.js',
        dest: 'panels/static/javascript/panels.js'
      }
    },
    compass: {
      dist: {
        options: {
          sassDir: 'panels/source/app/css',
          cssDir: 'panels/static/css',
          imagesDir: 'panels/static/images',
          javascriptsDir: 'panels/static/js',
          outputStyle: 'compressed',
          relativeAssets: true,
          noLineComments: true
        }
      }
    },
    concat: {
        dist: {
            files: {
                'panels/static/css/libs.css': [
                    'panels/source/vendors/font-awesome/css/font-awesome.min.css',
                ]
            }
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
  grunt.loadNpmTasks('grunt-contrib-compass');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-concat');

  // Default task(s).
  grunt.registerTask('default', ['uglify', 'compass', 'concat', 'copy']);


  grunt.registerTask('build', ['uglify']);
};