import frappe
from frappe.model.document import Document


class Customer(Document):
	pass


@frappe.whitelist(allow_guest=False)
def get_customers():
	"""Get list of customers"""
	return frappe.get_all(
		"Customer",
		fields=["name", "customer_name", "email", "phone", "role", "address"],
		order_by="modified desc",
		limit=50,
	)


@frappe.whitelist(allow_guest=False)
def create_customer(customer_name, email=None, phone=None, role=None, address=None):
	"""Create a new customer"""
	doc = frappe.get_doc({
		"doctype": "Customer",
		"customer_name": customer_name,
		"email": email,
		"phone": phone,
		"role": role,
		"address": address,
	})
	doc.insert()
	frappe.db.commit()
	return {"success": True, "name": doc.name}
