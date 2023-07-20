# In advika_enterprises/overrides/user.py

import frappe
from frappe import _
from frappe.utils import validate_email_address

@frappe.whitelist(allow_guest=True)
def sign_up(email, full_name, verify_terms, mobile_number):
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

        return user.name
    else:
        frappe.throw(_("Email ID is already registered"))
