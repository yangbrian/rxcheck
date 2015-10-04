var drugNames = ['CHANTECAILLE', 'Ipratropium Bromide', 'ECZEMA REAL RELIEF', 'Amnesteem'];
var conditions = ['pregnant', 'breast-feeding'];

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
        $.each(drugNames, function(index, value) {
            $.getJSON('/get/warnings/' + encodeURIComponent(value), function(data) {
                var warnings = data.warnings_and_precautions.length > data.warnings.length ? data.warnings_and_precautions : data.warnings;
                var row = $('<tr>');

                row.append('<td>' + data.brand_name + '</td>');
                row.append('<td>' + data.generic_name + '</td>');
                row.append('<td>' + warnings + '</td>');
                row.append('<td>' + data.active_ingredient + '</td>');
                row.append('<td>' + data.inactive_ingredient + '</td>');

                $('#resultTable').append(row);
            })
        })
    })
});