
function update_fields(pickup_date_field) {
    let date =  pickup_date_field.value;
    console.log(pickup_date_field.form)
    let parking = pickup_date_field.form.querySelector("#pickup_location").value
    console.log(date+parking)
}
