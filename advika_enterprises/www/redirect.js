frappe.ready(function() {
    frappe.call({
        method: 'advika_enterprises.redirect.get_context',
        callback: function(response) {
            // Callback function
        }
    });
});
