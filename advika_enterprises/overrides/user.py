# # In advika_enterprises/overrides/user.py

# import frappe
# from frappe import _
# from frappe.utils import validate_email_address

# @frappe.whitelist(allow_guest=True)
# def sign_up(email, full_name, verify_terms, mobile_number):
#     # Validate inputs
#     if not (email and full_name and mobile_number and verify_terms):
#         frappe.throw(_("Please fill all required fields"))
    
#     if not validate_email_address(email):
#         frappe.throw(_("Invalid email address"))
    
#     if not frappe.db.exists("User", email):
#         user = frappe.new_doc("User")
#         user.email = email
#         user.first_name = full_name
#         user.mobile_no = mobile_number
#         user.enabled = True
#         user.send_welcome_email = True
#         user.user_type = "Website User"
#         user.save(ignore_permissions=True)

#         # set default signup role as per Portal Settings
#         default_role = frappe.db.get_value("Portal Settings", None, "default_role")
#         if default_role:
#             user.add_roles(default_role)

#         return user.name
#     else:
#         frappe.throw(_("Email ID is already registered"))

# In advika_enterprises/overrides/user.py

import frappe
from frappe import _
from frappe.utils import validate_email_address

@frappe.whitelist(allow_guest=True)
def sign_up(email, full_name, verify_terms, mobile_number, customer_group, gst_category=None, gstin=None, pan=None):
    # Validate inputs
    if not (email and full_name and mobile_number and verify_terms):
        frappe.throw(_("Please fill all required fields"))
    
    if not validate_email_address(email):
        frappe.throw(_("Invalid email address"))
    
    if not frappe.db.exists("User", email):
        user = frappe.new_doc("User")
        user.email = email
        user.first_name = full_name
        user.mobile_no = mobile_number
        user.enabled = True
        user.send_welcome_email = True
        user.user_type = "Website User"
        user.save(ignore_permissions=True)

        # set default signup role as per Portal Settings
        default_role = frappe.db.get_value("Portal Settings", None, "default_role")
        if default_role:
            user.add_roles(default_role)

        # create customer entry
        customer = frappe.new_doc("Customer")
        customer.customer_name = full_name
        customer.customer_type = "Individual"
        customer.customer_group = customer_group
        if customer_group in ["Retailer", "Wholesaler"]:
            customer.gst_category = gst_category
            customer.gstin = gstin
            customer.pan = pan
        customer.save(ignore_permissions=True)
        
        return user.name
    else:
        frappe.throw(_("Email ID is already registered"))

@frappe.whitelist(allow_guest=True)
def get_customer_groups():
    allowed_groups = ["Individual", "Retailer", "Wholesaler"]
    customer_groups = frappe.get_all("Customer Group", filters={"name": ["in", allowed_groups]}, fields=["name"])
    return customer_groups
