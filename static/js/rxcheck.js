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

                $new.on('click', function() {
                   addDrug(value, suggestions);
                });
            });
        });
    });


});

function addDrug(value, suggestions) {
    if(drugNames.indexOf(value) == -1) {
        drugNames.push(value);

        var newItem = $('<li>');
        newItem.html(value);

        $('#drug-list').find('ul').append(newItem);
    }

    suggestions.fadeOut();
    suggestions.html('');
    $('.input-field').val('');


}

$(document).ready(function() {
    $('#warningsButton').on('click', function(e) {
        console.log('warning');
    })
});