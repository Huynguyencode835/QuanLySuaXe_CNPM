from flask import Flask, render_template


class ReceptionController():

    # [GET] /components
    def index(self):
        return render_template("receptions.html", page="Phiếu đặt lịch")
