from flask import render_template


class RepairFormController:
    def index(self):
        return render_template("repairform.html", page="Phiếu sửa xe")