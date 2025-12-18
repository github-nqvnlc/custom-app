frappe.ui.form.on('Customer', {
	// Hook chạy khi form load/reload
	refresh: function(frm) {
	},
	
	validate: function(frm) {
		// kiểm tra mail,phone
		if (!frm.doc.email && !frm.doc.phone) {
			frappe.throw('Vui lòng nhập Email hoặc Phone');
		}
		
		// email format
		if (frm.doc.email && !frm.doc.email.includes('@')) {
			frappe.throw('Email không hợp lệ');
		}
	},
	
});
