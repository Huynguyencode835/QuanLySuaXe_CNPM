from flask import Flask, render_template


class Create_receiptController:
    def index(self):
        return render_template("create_receipts.html", page="Lập hóa đơn")
