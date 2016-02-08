/*
 * Main Application
 */

var App = function() {

    var uiInit = function(){
        // Set variables
        $lHtml = jQuery('html');
        $lBody = jQuery('body');
        $lPage = jQuery('#page-container')
    };

    var uiLayoutApi = function($mode){
         var $windowW = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

        // Mode selection
        switch($mode) {
           case 'sidebar_toggle':
                if ($windowW > 991) {
                    $lPage.toggleClass('navigation__open');
                } else {
                    $lPage.toggleClass('navigation__open-xs');
                }
                break;
           case 'sidebar_open':
                if ($windowW > 991) {
                    $lPage.addClass('navigation__open');
                } else {
                    $lPage.addClass('navigation__open-xs');
                }
                break;
           case 'sidebar_close':
                if ($windowW > 991) {
                    $lPage.removeClass('navigation__open');
                } else {
                    $lPage.removeClass('navigation__open-xs');
                }
                break;
           case 'sidebar_mini_toggle':
                if ($windowW > 991) {
                    $lPage.toggleClass('navigation-mini');
                }
                break;
            case 'sidebar_mini_on':
                if ($windowW > 991) {
                    $lPage.addClass('navigation-mini');
                }
                break;
            case 'sidebar_mini_off':
                if ($windowW > 991) {
                    $lPage.removeClass('navigation-mini');
                }
                break;
           default:
                return false;
        }
    };

    var uiBlocksApi = function($block, $mode){

    };

    return {
        init: function ($func){
            uiInit()
        },
        layout: function($mode) {
            uiLayoutApi($mode);
        },
        blocks: function($block, $mode) {
            uiBlocksApi($block, $mode);
        }
    };
}();


// Initialize app when page loads
jQuery(function(){
    if (typeof angular == 'undefined') {
        App.init();
    }
});