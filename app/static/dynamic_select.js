
function update_fields(pickup_date_field) {
    let date =  pickup_date_field.value;
    let parking_id = pickup_date_field.form.elements["pickup_parking_id"].value;

    let not_available_times_form = document.getElementById('not_available_times_form');
    not_available_times_form.elements["pickup_date"].value = date;
    not_available_times_form.elements["pickup_parking_id"].value = parking_id;

    $.post(
        "/not_available_times",
        $('#not_available_times_form').serialize(),

        function( data ) {
            console.log( data );
        },

        "json",
    );
}
