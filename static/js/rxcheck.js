var drugNames = [];
var conditions = [];

$(document).ready(function() {
    $('.input-field').on('keyup', function(e) {
        $(this).siblings('.suggestions').fadeOut();
    });


});

$(document).ready(function() {
    $('#warningsButton').on('click', function(e) {
        console.log('warning');
    })
});