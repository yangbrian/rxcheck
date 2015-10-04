var drugNames = [];
var conditions = [];

var possibleConditions = [];

$(document).ready(function() {
    $('#drugs-input').on('keyup', function (e) {

        var suggestions = $(this).parent().siblings('.suggestions');
        suggestions.hide();

        $.getJSON('/get/names/' + encodeURIComponent($(this).val()), function (data) {

            console.log(data.length);

            if (data.length > 0)
                suggestions.fadeIn();

            $.each(data, function (index, value) {
                var $new = $('<div>');
                $new.addClass('suggestion');
                $new.html(value);

                suggestions.append($new);

                $new.on('click', function () {
                    addDrug(value, suggestions);
                });
            });
        });
    });

    $('#conditions-input').on('keyup', function () {
        var suggestions = $(this).parent().siblings('.suggestions');
        suggestions.fadeOut();
        suggestions.html('');

        var condValue = $(this).val();

        var fadeIn = false;
        for (var i = 0; i < possibleConditions.length; i++) {

            if (condValue === '') break;
            if (possibleConditions[i].indexOf(condValue) === 0) {

                if (!fadeIn) {
                    suggestions.fadeIn();
                    fadeIn = true;
                }
                var $new = $('<div>');
                $new.addClass('suggestion');
                $new.attr('data-value', possibleConditions[i]);
                $new.html(possibleConditions[i]);

                suggestions.append($new);

                console.log($new);

                $new.on('click', function () {
                    addCondition($(this).attr('data-value'), suggestions);
                });
            }
        }


    });
});

function addDrug(value, suggestions) {
    if(drugNames.indexOf(value) == -1) {
        drugNames.push(value);

        var newItem = $('<li>');
        newItem.addClass('list-group-item clearfix');
        newItem.append('<span class="itemListElement">' + value + '</span>');
        newItem.append('<button class="btn btn-error closeBtn" onclick="removeDrug(this);">x</button>');

        $('#selected-drugs').find('ul').append(newItem);
    }

    suggestions.fadeOut();
    suggestions.html('');
    $('#drugs-input').val('');

}

function addCondition(value, suggestions) {
    if(conditions.indexOf(value) == -1) {
        conditions.push(value);

        var newItem = $('<li>');
        newItem.addClass('list-group-item clearfix');
        newItem.append('<span class="itemListElement">' + value + '</span>');
        newItem.append('<button class="btn btn-error closeBtn" onclick="removeCondition(this);">x</button>');
        //newItem.html(value);

        $('#selected-conditions').find('ul').append(newItem);
    }

    suggestions.fadeOut();
    suggestions.html('');
    $('#drugs-input').val('');

}

$(document).ready(function() {
    $('#warningsButton').on('click', function(e) {
        reloadTable();
    })
});

function reloadTable() {
    //clear table first
    $('#resultTable tr').has('td').remove();

    $.each(drugNames, function(index, value) {
        $.getJSON('/get/warnings/' + encodeURIComponent(value), function(data) {
            var warnings = String(data.warnings_and_precautions.length > data.warnings.length ? data.warnings_and_precautions : data.warnings);
            var row = $('<tr>');

            //Parse through text. If any of the conditions are said, bold it.
            $.each(conditions, function(index, value) {
                if (warnings.indexOf(value) != -1)
                    row.addClass('warning');
                var re = new RegExp(value, "gi");
                warnings = warnings.replace(re, ('<strong>' + value + '</strong>'));
            });

            row.append('<td>' + data.brand_name + '</td>');
            row.append('<td>' + data.generic_name + '</td>');
            row.append('<td>' + warnings + '</td>');
            row.append('<td>' + data.active_ingredient + '</td>');
            row.append('<td>' + data.inactive_ingredient + '</td>');

            $('#resultTable').append(row);
        })
    })
}

function removeDrug(el) {
    var drug = $(el).parent().children(":first").html();
    drugNames.splice(drugNames.indexOf(drug), 1);
    $(el).parent().remove();
    reloadTable();
}

function removeCondition(el) {
    var condition = $(el).parent().children(":first").html();
    conditions.splice(conditions.indexOf(condition), 1);
    $(el).parent().remove();
    reloadTable();
}