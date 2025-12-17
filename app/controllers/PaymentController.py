from flask import Flask, render_template
import app.dao.dao as dao

class PaymentController():
    def index(self):
        receipt = dao.get_unpaid_receipt(1)
        return render_template("payment.html",page="Thanh toán",receipt=receipt)