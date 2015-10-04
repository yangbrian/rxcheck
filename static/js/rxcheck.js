var drugNames = [];
var conditions = [];

$(document).ready(function() {
    $('.input-field').on('keyup', function(e) {

        var input = $(this);
        $.getJSON( '/get/names/' + encodeURIComponent($(this).val()), function( data ) {
            var suggestions = input.parent().siblings('.suggestions');

            console.log(data.length);

            if (data.length > 0)
                suggestions.fadeIn();

            $.each(data, function(index, value) {
                var $new = $('<div>');
                $new.addClass('suggestion');
                $new.html(value);

                suggestions.append($new);
            });
        });
    });


});

$(document).ready(function() {
    $('#warningsButton').on('click', function(e) {
        console.log('warning');
    })
});