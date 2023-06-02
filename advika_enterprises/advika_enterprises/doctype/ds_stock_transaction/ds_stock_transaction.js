// Copyright (c) 2023, MD Faiyaz Ansari and contributors
// For license information, please see license.txt

// frappe.ui.form.on("DS Stock Transaction", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('DS Stock Transaction', {
    item_code: function(frm) {
        if(frm.doc.item_code){
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'DS Stock',
                    name: frm.doc.item_code
                },
                callback: function(response) {
                    let ds_stock = response.message;
                    if(ds_stock){
                        frm.set_value('current_stock', ds_stock.available_stock);
                    }else{
                        frm.set_value('current_stock', null);
                    }
                }
            });
        }else{
            frm.set_value('current_stock', null);
        }
    },

    after_save: function(frm) {
        var interval = setInterval(function(){
            if(!frm.is_saving){
                clearInterval(interval);
                frappe.call({
                    method: 'frappe.client.get',
                    args: {
                        doctype: 'DS Stock',
                        name: frm.doc.item_code
                    },
                    callback: function(response) {
                        let ds_stock = response.message;
                        if(ds_stock){
                            frappe.show_alert(`Current available stock: ${ds_stock.available_stock}`);
                          
                            frappe.msgprint({
                                title: __('Updated Stock'),
                                indicator: 'green',
                                message: `<div style="text-align: center;">Current available stock: ${ds_stock.available_stock}</div>`
                            });
                         


                           
                        }
                    }
                });
            }
        }, 100);
    }
});
