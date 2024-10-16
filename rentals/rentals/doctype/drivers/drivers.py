# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Drivers(Document):
	def before_save(self):  #controllers
		self.full_name = f"{self.first_name} {self.last_name}"

