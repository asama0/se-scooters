
function update_fields(pickup_date_field) {
    let booking_form = pickup_date_field.form;
    let date =  pickup_date_field.value;
    let parking_id = booking_form.elements["pickup_parking_id"].value;

    let not_available_times_form = document.getElementById('not_available_times_form');
    not_available_times_form.elements["pickup_date"].value = date;
    not_available_times_form.elements["pickup_parking_id"].value = parking_id;

    $.post(
        "/not_available_times",
        $('#not_available_times_form').serialize(),

        function(data) {
            if (data['all']) {
                pickup_date_field.setCustomValidity("This day is Fully booked");
                booking_form.elements["pickup_time"].disabled = true;
                booking_form.elements["time_period"].disabled = true;
                booking_form.elements["submit"].click();
            } else {
                pickup_date_field.setCustomValidity("");
                booking_form.elements["pickup_time"].disabled = false;
                booking_form.elements["time_period"].disabled = false;
            }
        },

        "json",
    );
}
