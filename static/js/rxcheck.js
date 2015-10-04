var drugNames = ['CHANTECAILLE', 'Ipratropium Bromide', 'ECZEMA REAL RELIEF', 'Amnesteem'];
var conditions = ['pregnant', 'breast-feeding'];

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