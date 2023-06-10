// Copyright (c) 2023, MD Faiyaz Ansari and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Supplier Order Confirmation", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Supplier Order Confirmation', {
    refresh: function(frm) {
        if (frappe.user.has_role('Administrator')) {
            frm.add_custom_button(__('Create Invoice'), function() {
                // Get the purchase order from the current Supplier Order Confirmation
                let purchase_order = frm.doc.purchase_order;

                // Check if a purchase order was found
                if (purchase_order) {
                    // Navigate to the Purchase Order document
                    frappe.set_route("Form", "Purchase Order", purchase_order);
                } else {
                    frappe.msgprint(__("Please select a Purchase Order first."));
                }
            });
        }
    },
});

// frappe.ui.form.on('Supplier Order Confirmation', {
//     refresh: function(frm) {
//         // clear existing primary action
//         frm.page.clear_primary_action();

//         // add your custom primary action
//         frm.page.set_primary_action(__('Create Invoice'), function() {
//             // Get the purchase order from the current Supplier Order Confirmation
//             let purchase_order = frm.doc.purchase_order;

//             // Check if a purchase order was found
//             if (purchase_order) {
//                 // Navigate to the Purchase Order document
//                 frappe.set_route("Form", "Purchase Order", purchase_order);
//             } else {
//                 frappe.msgprint(__("Please select a Purchase Order first."));
//             }
//         });
//     },
// });
