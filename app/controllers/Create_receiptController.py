from flask import Flask, render_template,request,jsonify,abort,send_file
from datetime import datetime
import app.dao.dao as dao
from app.models.model import RepairForm,Receipt,SystemParameters
from flask_login import current_user, login_required
from app._init_ import db
from app.utils import receptionform_util,calc_total_repairform

class Create_receiptController:
    def index(self):
        rp_f=dao.get_repair_form()
        return render_template("create_receipts.html",
                               page="Lập hóa đơn",rp_f=rp_f,
                               state=receptionform_util.parse_state())

    def create_receipt(self):
        data = request.get_json()
        repair_form_ids = data.get("repair_form_ids", [])

        if not repair_form_ids:
            return jsonify({"error": "Chưa chọn phiếu sửa"}), 400

        repair_forms = RepairForm.query.filter(
            RepairForm.id.in_(repair_form_ids),
            RepairForm.receipt_id == None
        ).all()

        if not repair_forms:
            return jsonify({"error": "Phiếu sửa không hợp lệ"}), 400

        total_component_cost = calc_total_repairform.calc_total_component(repair_forms)
        total_labor_cost=calc_total_repairform.calc_labor_cost(repair_forms)
        total_cost = calc_total_repairform.calc_total_VAT(repair_forms)
        receipt = Receipt(
            total_labor_cost=total_labor_cost,
            total_component_cost=total_component_cost,
            total_cost=total_cost,
            customer_id=repair_forms[0].reception_form.customer_id,
            accountant_id=current_user.id,
            created_date=datetime.now()
        )

        db.session.add(receipt)
        db.session.flush()

        for rf in repair_forms:
            rf.receipt_id = receipt.id

        updated_receptions = set()

        for rf in repair_forms:
            reception = rf.reception_form
            if reception.id not in updated_receptions:
                reception.status = receptionform_util.Form_status.SUCCESS
                updated_receptions.add(reception.id)

        db.session.commit()

        return jsonify({
            "receipt_id": receipt.id,
            "total_labor_cost": total_labor_cost,
            "total_component_cost": total_component_cost
        })





