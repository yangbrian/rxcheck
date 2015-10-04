$(document).ready(function() {
    $('.input-field').on('keyup', function(e) {
        $(this).siblings('.suggestions').fadeOut();
    });


});