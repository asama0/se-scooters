function update_durations(dutration_select) {
    let extension_form = dutration_select.form;
    let booking_id = extension_form.elements["booking_id"].value

    let not_available_durations_form = document.getElementById('not_available_durations_form');
    not_available_durations_form.elements["booking_id"].value = booking_id;

    $.post(
        "/not_available_durations",
        $('#not_available_durations_form').serialize(),

        function(data) {
            data.forEach(duration_id => {
                for (let i=0; i < dutration_select.options.length; i++) {
                    if (dutration_select.options[i].value == duration_id){
                        dutration_select.options[i].disabled = true;
                    }
                }
            });
        },

        "json",
    );
}
