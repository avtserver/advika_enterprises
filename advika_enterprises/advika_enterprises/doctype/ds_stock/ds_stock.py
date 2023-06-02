# Copyright (c) 2023, MD Faiyaz Ansari and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class DSStock(Document):
# 	pass
# frappe framework

# import frappe

from frappe.model.document import Document

class DSStock(Document):
    def validate(self):
        self.update_stock()

    def update_stock(self):
        if self.available_stock is None:
            self.available_stock = 0

        if self.add_stock:
            self.available_stock += self.add_stock
            self.add_stock = 0  # Reset the field for the next transaction

        if self.sold_stock:
            self.available_stock -= self.sold_stock
            self.sold_stock = 0  # Reset the field for the next transaction
