
// JavaScript Tabs
$(function() {

    $('.vds-tabs--default .vds-tabs--default__item').on('click', function(){
        // Hide all tabs
        tab = $(this);

        tabs = tab.closest('.vds-tabs--default');
        tabs.find('.vds-tabs--default__content').addClass('vds-hide').removeClass('vds-show');
        tabs.find('.vds-tabs--default__item').removeClass('vds-active');

        // Current Tab
        tab.addClass('vds-active');
        tabs.find('#'+tab.attr('aria-controls')).addClass('vds-show');
    });
});