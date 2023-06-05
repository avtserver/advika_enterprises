import frappe
from frappe.model.document import Document

def create_ds_stock(doc, method):
    if doc.is_new():
        # Create new DS Stock document
        ds_stock = frappe.get_doc({
            "doctype": "DS Stock",
            "item_code": doc.item_code,
            "item_name": doc.item_name,
            "available_stock": doc.ds_initial_stock,  # Set available_stock to Item's ds_initial_stock
        })
        ds_stock.insert(ignore_permissions=True)
