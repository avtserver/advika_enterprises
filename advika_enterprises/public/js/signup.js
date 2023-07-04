frappe.ready(function() {
    // Add mobile_no input to the form
    $('<input>').attr({
        type: 'tel',
        id: 'mobile_no',
        name: 'mobile_no',
        required: 'required',
        placeholder: 'Mobile Number'
    }).insertAfter('#id_password');

    // Override the click event for the sign up button
    $('.btn-form-submit').on('click', function(e) {
        e.preventDefault();

        // Get form data
        var data = frappe.utils.get_form_data(this.form);
        data.cmd = 'frappe.core.doctype.user.user.sign_up';
        data.mobile_no = $('#mobile_no').val();

        // Send signup request
        login.call(data);
    });
});
