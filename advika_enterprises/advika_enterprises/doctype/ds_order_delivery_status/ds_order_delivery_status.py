# Copyright (c) 2023, MD Faiyaz Ansari and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class DSOrderDeliveryStatus(Document):
# 	pass


from frappe.model.document import Document
import frappe
from frappe.utils import nowdate
# NameError: name '_' is not defined
from frappe import _

class DSOrderDeliveryStatus(Document):
    pass


# sales order

@frappe.whitelist()
def create_status_and_log(doc, method):
    # doc here represents the Sales Order document

    # Create DS Order Delivery Status document
    delivery_status = frappe.new_doc('DS Order Delivery Status')
    delivery_status.sales_order = doc.name
    delivery_status.ds_order_status = 'Pending'
    # delivery_status.sales_order_item = ", ".join([item.item_code for item in doc.items]) # Commented out
    delivery_status.status_updated_on = nowdate()
    # delivery_status.comment = 'Sales order submitted.'
    delivery_status.comment = 'Sales order {} submitted.'.format(doc.name)
    
    delivery_status.save()
    
    # Create DS Order Status Log document and append it to the parent document
    status_log = delivery_status.append('status_logs', {})
    status_log.new_status = 'Pending'
    status_log.change_time = nowdate()
    status_log.changed_by = frappe.session.user  # Capture the current user
    status_log.sales_order = doc.name
    status_log.comment = 'Sales order submitted.'
	# status_log.comment = 'Sales order {} submitted.'.format(doc.name)
    
    

    # Save DS Order Delivery Status document which also saves the child table 'DS Order Status Log'
    delivery_status.save()
        # Print a message
    frappe.msgprint(_("DS Order Status Updated to {0}").format(status_log.new_status))

#sale invoice

@frappe.whitelist()
def update_status_and_log(doc, method):
    # doc here represents the Sales Invoice document

    # Retrieve the name of the sales order from the first item in the sales invoice
    # Make sure all the items in your sales invoice belong to the same sales order
    sales_order = doc.items[0].sales_order if doc.items else None

    # Check if a sales order was found
    if sales_order:
        # Retrieve the existing DS Order Delivery Status document
        try:
            delivery_status = frappe.get_doc('DS Order Delivery Status', {'sales_order': sales_order})
        except frappe.DoesNotExistError:
            frappe.throw(_("DS Order Delivery Status for Sales Order {0} not found.").format(sales_order))
        
        # Capture the previous status before updating it
        previous_status = delivery_status.ds_order_status
        delivery_status.ds_order_status = 'Paid'
        delivery_status.status_updated_on = nowdate()
        delivery_status.comment = 'Sales invoice {} submitted.'.format(doc.name)

        # Append a new status log to the document
        status_log = delivery_status.append('status_logs', {})
        status_log.sales_order = sales_order  # Set the sales_order in the child table
        status_log.previous_status = previous_status  # Add the previous status to the log
        status_log.new_status = 'Paid'
        status_log.change_time = nowdate()
        status_log.changed_by = frappe.session.user  # Capture the current user
        status_log.comment = 'Sales invoice {} submitted.'.format(doc.name)

        # Save the changes to DS Order Delivery Status document which also saves the new status log
        delivery_status.save()

        # Print a message
        frappe.msgprint(_("DS Order Status Updated to {0}").format(status_log.new_status))
    else:
        frappe.throw(_("Sales Order not found in Sales Invoice items."))



# Purchase Order Hook

@frappe.whitelist()
def update_status_and_log_on_po_submit(doc, method):
    # doc here represents the Purchase Order document

    # Retrieve the name of the sales order from the first item in the purchase order
    # Make sure all the items in your purchase order belong to the same sales order
    sales_order = doc.items[0].sales_order if doc.items else None

    # Check if a sales order was found
    if sales_order:
        # Retrieve the existing DS Order Delivery Status document
        try:
            delivery_status = frappe.get_doc('DS Order Delivery Status', {'sales_order': sales_order})
        except frappe.DoesNotExistError:
            frappe.throw(_("DS Order Delivery Status for Sales Order {0} not found.").format(sales_order))
        
        # Capture the previous status before updating it
        previous_status = delivery_status.ds_order_status
        delivery_status.ds_order_status = 'Supplier Received Order'
        delivery_status.status_updated_on = nowdate()
        delivery_status.purchase_order = doc.name
        delivery_status.comment = 'Purchase order {} submitted. Status updated to {}.'.format(doc.name, delivery_status.ds_order_status)

        # Append a new status log to the document
        status_log = delivery_status.append('status_logs', {})
        status_log.sales_order = sales_order  # Set the sales_order in the child table
        status_log.previous_status = previous_status  # Add the previous status to the log
        status_log.new_status = 'Supplier Received Order'
        status_log.change_time = nowdate()
        status_log.changed_by = frappe.session.user  # Capture the current user
        status_log.comment = 'Purchase order {} submitted. Status updated to {}.'.format(doc.name, status_log.new_status)

        # Save the changes to DS Order Delivery Status document which also saves the new status log
        delivery_status.save()

        # Print a message
        frappe.msgprint(_("DS Order Status Updated to {0}").format(status_log.new_status))
    else:
        frappe.throw(_("Sales Order not found in Purchase Order items."))


# Purchase Order Hook
# Purchase Invoice Hook
@frappe.whitelist()
def update_status_and_log_on_pi_submit(doc, method):
    # doc here represents the Purchase Invoice document

    # Retrieve the name of the purchase order from the first item in the purchase invoice
    purchase_order = doc.items[0].purchase_order if doc.items else None

    # Check if a purchase order was found
    if purchase_order:
        # Retrieve the purchase order document
        purchase_order_doc = frappe.get_doc('Purchase Order', purchase_order)
        
        # Retrieve the name of the sales order from the first item in the purchase order
        sales_order = purchase_order_doc.items[0].sales_order if purchase_order_doc.items else None

        if not sales_order:
            frappe.throw(_("Sales Order not found in Purchase Order items."))
        
        # Retrieve the existing DS Order Delivery Status document
        try:
            delivery_status = frappe.get_doc('DS Order Delivery Status', {'sales_order': sales_order})
        except frappe.DoesNotExistError:
            frappe.throw(_("DS Order Delivery Status for Sales Order {0} not found.").format(sales_order))

        # Capture the previous status before updating it
        previous_status = delivery_status.ds_order_status
        delivery_status.ds_order_status = 'Item shipped by Supplier'
        delivery_status.status_updated_on = nowdate()
        delivery_status.purchase_invoice = doc.name
        delivery_status.comment = 'Purchase invoice {} submitted. Status updated to {}.'.format(doc.name, delivery_status.ds_order_status)

        # Append a new status log to the document
        status_log = delivery_status.append('status_logs', {})
        status_log.sales_order = sales_order  # Set the sales_order in the child table
        status_log.previous_status = previous_status  # Add the previous status to the log
        status_log.new_status = 'Item shipped by Supplier'
        status_log.change_time = nowdate()
        status_log.changed_by = frappe.session.user  # Capture the current user
        status_log.comment = 'Purchase invoice {} submitted. Status updated to {}.'.format(doc.name, status_log.new_status)

        # Save the changes to DS Order Delivery Status document which also saves the new status log
        delivery_status.save()

        # Print a message
        frappe.msgprint(_("DS Order Status Updated to {0}").format(status_log.new_status))
    else:
        frappe.throw(_("Purchase Order not found in Purchase Invoice items."))

# create delivery boy status entry for further order status update

@frappe.whitelist()
def create_delivery_boy_status_on_pi_submit(doc, method):
    # Retrieve the name of the purchase order from the first item in the purchase invoice
    purchase_order = doc.items[0].purchase_order if doc.items else None

    # Check if a purchase order was found
    if purchase_order:
        # Create a new Delivery Boy Status document
        delivery_boy_status = frappe.new_doc('Delivery Boy Status')

        # Set the purchase order and purchase invoice fields
        delivery_boy_status.purchase_order = purchase_order
        delivery_boy_status.purchase_invoice = doc.name

        # Save the document as a draft
        delivery_boy_status.save()

        # Print a message
        frappe.msgprint(_("Delivery Boy Status document created for <b>further order updates</b>."))
    else:
        frappe.throw(_("Purchase Order not found in Purchase Invoice items."))


# further order status update by Delivery Boy Status document
@frappe.whitelist()
def update_ds_order_delivery_status_on_db_save(doc, method):
    # doc here represents the Delivery Boy Status document

    # Retrieve the purchase order
    purchase_order_doc = frappe.get_doc('Purchase Order', doc.purchase_order)
    sales_order = purchase_order_doc.items[0].sales_order if purchase_order_doc.items else None

    # Check if a sales order was found
    if sales_order:
        # Retrieve the existing DS Order Delivery Status document
        delivery_status = frappe.get_doc('DS Order Delivery Status', {'sales_order': sales_order})

        # Get the latest status update from Delivery Boy Status
        latest_status_update = doc.ds_db_status_update[-1] if doc.ds_db_status_update else None

        if latest_status_update:
            # Capture the previous status before updating it
            previous_status = delivery_status.ds_order_status

            if latest_status_update.status == 'Item Received':
                # Update DS Order Delivery Status
                delivery_status.ds_order_status = 'Item has been picked up by Delivery Boy'

            elif latest_status_update.status == 'Out for delivery':
                # Update DS Order Delivery Status
                delivery_status.ds_order_status = 'Item is out for delivery'

            elif latest_status_update.status == 'Delivered':
                # Update DS Order Delivery Status
                delivery_status.ds_order_status = 'Item has been delivered'

            delivery_status.status_updated_on = nowdate()
            delivery_status.comment = 'Status updated to {} on update of Delivery Boy Status {}.'.format(delivery_status.ds_order_status, doc.name)

            # Append a new status log to the DS Order Delivery Status document
            status_log = delivery_status.append('status_logs', {})
            status_log.sales_order = sales_order  # Set the sales_order in the child table
            status_log.previous_status = previous_status  # Add the previous status to the log
            status_log.new_status = delivery_status.ds_order_status
            status_log.change_time = nowdate()
            status_log.changed_by = frappe.session.user  # Capture the current user
            status_log.comment = 'Status updated to {} on update of Delivery Boy Status {}.'.format(status_log.new_status, doc.name)

            # Save the changes to DS Order Delivery Status document which also saves the new status log
            delivery_status.save()

            # Print a message
            frappe.msgprint(_("DS Order Status Updated to {0}").format(status_log.new_status))
        else:
            frappe.throw(_("No status update found in Delivery Boy Status updates."))
    else:
        frappe.throw(_("Sales Order not found in Purchase Order items."))
