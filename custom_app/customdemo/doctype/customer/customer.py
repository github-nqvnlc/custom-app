import frappe
from frappe.model.document import Document


class Customer(Document):
	def validate(self):
		"""Chạy tự động khi save (cả Desk UI và API)"""
		# kiểm tra mail,phone
		if not self.email and not self.phone:
			frappe.throw("Vui lòng nhập Email hoặc Phone")
		
		# fortmat email
		if self.email and '@' not in self.email:
			frappe.throw("Email không hợp lệ")
	
	def before_save(self):
		"""Chạy trước khi save"""
		pass
	
	def after_insert(self):
		"""Chạy sau khi insert thành công"""
		pass


@frappe.whitelist(allow_guest=False)
def get_customers():
	"""Get list customers"""
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
