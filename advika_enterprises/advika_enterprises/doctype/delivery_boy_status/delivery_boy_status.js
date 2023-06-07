// Copyright (c) 2023, MD Faiyaz Ansari and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Delivery Boy Status", {
// 	refresh(frm) {

// 	},
// });
// frappe.ui.form.on('Delivery Boy Status', {
//     refresh: function(frm) {
//         // Here we add custom actions to the form toolbar
//         frm.add_custom_button(__('Item Received'), function() {
//             // What happens when 'Item Received' is clicked
//             // You could create a new child doc here and update the fields as required
//             let child = frm.add_child('ds_db_status_update');
//             child.status = 'Item Received';
//             child.update_on = frappe.datetime.now_datetime();
//             child.update_by = frappe.session.user;
//             frm.refresh_field('ds_db_status_update');
//         });

//         frm.add_custom_button(__('Out for delivery'), function() {
//             // What happens when 'Out for Delivery' is clicked
//             let child = frm.add_child('ds_db_status_update');
//             child.status = 'Out for delivery';
//             child.update_on = frappe.datetime.now_datetime();
//             child.update_by = frappe.session.user;
//             frm.refresh_field('ds_db_status_update');
//         });

//         frm.add_custom_button(__('Delivered'), function() {
//             // What happens when 'Delivered' is clicked
//             let child = frm.add_child('ds_db_status_update');
//             child.status = 'Delivered';
//             child.update_on = frappe.datetime.now_datetime();
//             child.update_by = frappe.session.user;
//             frm.refresh_field('ds_db_status_update');
//             // Submit the document
//             frm.save('Submit');
//         });
//     },
// });

// 2
// frappe.ui.form.on('Delivery Boy Status', {
//     refresh: function(frm) {
//         // Flag to track the clicked state of each button
//         var itemReceivedClicked = false;
//         var outForDeliveryClicked = false;
//         var deliveredClicked = false;

//         frm.add_custom_button(__('Item Received'), function() {
//             if (!itemReceivedClicked) {
//                 itemReceivedClicked = true;

//                 // What happens when 'Item Received' is clicked
//                 // You could create a new child doc here and update the fields as required
//                 let child = frm.add_child('ds_db_status_update');
//                 child.status = 'Item Received';
//                 child.update_on = frappe.datetime.now_datetime();
//                 child.update_by = frappe.session.user;
//                 frm.refresh_field('ds_db_status_update');
//             }
//         });

//         frm.add_custom_button(__('Out for delivery'), function() {
//             if (!outForDeliveryClicked) {
//                 outForDeliveryClicked = true;

//                 // What happens when 'Out for Delivery' is clicked
//                 let child = frm.add_child('ds_db_status_update');
//                 child.status = 'Out for delivery';
//                 child.update_on = frappe.datetime.now_datetime();
//                 child.update_by = frappe.session.user;
//                 frm.refresh_field('ds_db_status_update');
//             }
//         });

//         frm.add_custom_button(__('Delivered'), function() {
//             if (!deliveredClicked) {
//                 deliveredClicked = true;

//                 // What happens when 'Delivered' is clicked
//                 let child = frm.add_child('ds_db_status_update');
//                 child.status = 'Delivered';
//                 child.update_on = frappe.datetime.now_datetime();
//                 child.update_by = frappe.session.user;
//                 frm.refresh_field('ds_db_status_update');
//                 // Submit the document
//                 frm.save('Submit');
//             }
//         });
//     },
// });
// 3
frappe.ui.form.on('Delivery Boy Status', {
    refresh: function(frm) {
        // Flag to track the clicked state of each button
        var itemReceivedClicked = false;
        var outForDeliveryClicked = false;
        var deliveredClicked = false;

        frm.add_custom_button(__('Item Received'), function() {
            if (!itemReceivedClicked) {
                itemReceivedClicked = true;

                // What happens when 'Item Received' is clicked
                // You could create a new child doc here and update the fields as required
                let child = frm.add_child('ds_db_status_update');
                child.status = 'Item Received';
                child.update_on = frappe.datetime.now_datetime();
                child.update_by = frappe.session.user;
                frm.refresh_field('ds_db_status_update');
            }
        });

        frm.add_custom_button(__('Out for delivery'), function() {
            if (!outForDeliveryClicked) {
                outForDeliveryClicked = true;

                // What happens when 'Out for Delivery' is clicked
                let child = frm.add_child('ds_db_status_update');
                child.status = 'Out for delivery';
                child.update_on = frappe.datetime.now_datetime();
                child.update_by = frappe.session.user;
                frm.refresh_field('ds_db_status_update');
            }
        });

        frm.add_custom_button(__('Delivered'), function() {
            if (!deliveredClicked) {
                frappe.call({
                    method: 'frappe.client.get',
                    args: {
                        doctype: 'DS Order Delivery Status',
                        filters: {
                            'purchase_order': frm.doc.purchase_order
                        }
                    },
                    callback: function(response) {
                        var sales_invoice = response.message.sales_invoice;
                        frappe.call({
                            method: 'frappe.client.get',
                            args: {
                                doctype: 'Sales Invoice',
                                name: sales_invoice
                            },
                            callback: function(r) {
                                if (r.message.status === 'Paid') {
                                    deliveredClicked = true;
                                    
                                    // What happens when 'Delivered' is clicked
                                    let child = frm.add_child('ds_db_status_update');
                                    child.status = 'Delivered';
                                    child.update_on = frappe.datetime.now_datetime();
                                    child.update_by = frappe.session.user;
                                    frm.refresh_field('ds_db_status_update');
                                    // Submit the document
                                    frm.save('Submit');
                                } else {
                                    // frappe.msgprint(__('Please make the payment for this order first.'));
                                    frappe.msgprint(__('Please make the payment for this order first. You can pay it <a href="/app/sales-invoice/'+sales_invoice+'">here</a>.'));                        
                                }
                            }
                        });
                    }
                });
            }
        });
    },
});
