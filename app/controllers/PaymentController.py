from flask import Flask, render_template, request, flash, redirect, url_for,abort,send_file
from flask_login import current_user, login_required

import app.dao.dao as dao
from app.utils.receptionform_util import Form_status
from app.utils.pdf_util import export_receipt_pdf
from app._init_ import db


class PaymentController():
    @login_required
    def index(self):
        receipt = dao.get_my_unpaid_receipt(current_user.id)
        # POST = xác nhận thanh toán
        if request.method == 'POST':
            try:
                receipt.status = Form_status.SUCCESS
                receipt.paid_by = "CUSTOMER"

                for rf in receipt.repair_forms:
                    rf.status = Form_status.SUCCESS

                    if rf.reception_form:
                        rf.reception_form.status = Form_status.SUCCESS

                db.session.commit()

                flash("Thanh toán thành công!", "success")
                return redirect(url_for(
                    'payments_bp.index',
                    receipt_id=receipt.id
                ))
            except Exception as e:
                db.session.rollback()
                flash("Lỗi khi thanh toán, vui lòng thử lại", "danger")
        return render_template("payment.html", page="Thanh toán", receipt=receipt)

