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

  // Default task(s).
  grunt.registerTask('default', ['uglify', 'sass', 'copy']);

  grunt.registerTask('build', ['uglify']);
};