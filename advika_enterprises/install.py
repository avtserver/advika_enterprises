import frappe
from frappe import _

def after_install():
    create_customer_groups()
    create_price_lists()

def create_customer_groups():
    default_customer_groups = ["Retailer", "Wholesaler"]
    for customer_group in default_customer_groups:
        if not frappe.db.exists('Customer Group', customer_group):
            frappe.get_doc({
                "doctype": "Customer Group",
                "customer_group_name": customer_group,
                "parent_customer_group": _("All Customer Groups"),
                "is_group": "No"
            }).insert()

def create_price_lists():
    default_price_lists = [
        {"name": "Retailer Selling Price", "selling": 1},
        {"name": "Wholesaler Selling Price", "selling": 1}
    ]
    for price_list in default_price_lists:
        if not frappe.db.exists('Price List', price_list["name"]):
            new_price_list = frappe.get_doc({
                "doctype": "Price List",
                "price_list_name": price_list["name"],
                "enabled": 1,
                "buying": 0,
                "selling": price_list["selling"],
                "currency": "INR"
            })
            new_price_list.append('countries', {
                'country': 'India'
            })
            new_price_list.insert()
