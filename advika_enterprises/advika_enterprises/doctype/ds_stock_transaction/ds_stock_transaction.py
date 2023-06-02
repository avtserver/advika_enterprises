# Copyright (c) 2023, MD Faiyaz Ansari and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class DSStockTransaction(Document):
# 	pass
# from __future__ import unicode_literals
# import frappe
# from frappe.model.document import Document

# class DSStockTransaction(Document):
#     def validate(self):
#         # your validation logic here
#         self.update_stock_in_ds_stock()

#     def update_stock_in_ds_stock(self):
#         # Your logic to fetch DS Stock Document using self.item_code and then
#         # add or subtract the self.add_stock or self.sold_stock amount from it.
#         ds_stock_doc = frappe.get_doc("DS Stock", self.item_code)

#         if self.add_stock:
#             ds_stock_doc.available_stock += self.add_stock
#         if self.sold_stock:
#             ds_stock_doc.available_stock -= self.sold_stock

#         ds_stock_doc.save()

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class DSStockTransaction(Document):
    def __init__(self, *args, **kwargs):
        super(DSStockTransaction, self).__init__(*args, **kwargs)

        # If the document is new and date_of_transaction is not set, set it to today's date
        if self.is_new() and not self.date_of_transaction:
            self.date_of_transaction = nowdate()

    def validate(self):
        # your validation logic here
        self.update_stock_in_ds_stock()

    def update_stock_in_ds_stock(self):
        # Your logic to fetch DS Stock Document using self.item_code and then
        # add or subtract the self.add_stock or self.sold_stock amount from it.
        ds_stock_doc = frappe.get_doc("DS Stock", self.item_code)

        if self.add_stock:
            ds_stock_doc.available_stock += self.add_stock
        if self.sold_stock:
            ds_stock_doc.available_stock -= self.sold_stock

        ds_stock_doc.save()

