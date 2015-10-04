var drugNames = [];
var conditions = [];

$(document).ready(function() {
    $('#drugs-input').on('keyup', function(e) {

        var suggestions = $(this).parent().siblings('.suggestions');
        suggestions.fadeOut();
        suggestions.html('');

        $.getJSON( '/get/names/' + encodeURIComponent($(this).val()), function( data ) {

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
        newItem.addClass('list-group-item');
        newItem.html(value);

        $('#selected-drugs').find('ul').append(newItem);
    }

    suggestions.fadeOut();
    suggestions.html('');
    $('#drugs-input').val('');


}

$(document).ready(function() {
    $('#warningsButton').on('click', function(e) {
        console.log('warning');
    })
});