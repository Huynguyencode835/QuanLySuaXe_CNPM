from flask import Flask, render_template,request
from app.dao.dao import get_repair_form,get_reception_form
import app.dao.dao as dao
from app.utils.calc_total_repairform import calc_labor_cost,calc_component_cost,calc_total_cost

class Create_receiptController:
    def index(self):
        q = request.args.get('q')
        rp_f=dao.load_repairform_receptionform(q=q)
        for rf in rp_f:
            rf.total_labor_cost = calc_labor_cost(rf)
            rf.total_component_cost = calc_component_cost(rf)
            rf.total_cost = calc_total_cost(rf)
        return render_template("create_receipts.html", page="Lập hóa đơn",rp_f=rp_f)
