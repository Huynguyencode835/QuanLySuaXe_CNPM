from flask import Flask, render_template
from app.dao.dao import get_repair_form
from app.utils.calc_total_repairform import calc_labor_cost,calc_component_cost,calc_total_cost

class Create_receiptController:
    def index(self):
        repair_forms= get_repair_form()
        for rf in repair_forms:
            rf.total_labor_cost = calc_labor_cost(rf)
            rf.total_component_cost = calc_component_cost(rf)
            rf.total_cost = calc_total_cost(rf)
        return render_template("create_receipts.html", page="Lập hóa đơn",repair_forms=repair_forms)
