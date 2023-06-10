# Fetch all Sales Orders
import frappe


sales_orders = frappe.get_all('Sales Order', fields=['name'])

counter = 0

# Check each Sales Order for linked Purchase Orders
for so in sales_orders:
    linked_pos = frappe.get_all('Purchase Order',
                               filters={'sales_order': so['name']},
                               fields=['name'])
    if not linked_pos:
        counter += 1

# Display the counter in a Number Card
frappe.publish_realtime('number_card', counter, user=frappe.session.user)
