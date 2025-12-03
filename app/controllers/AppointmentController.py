from flask import Flask, render_template


class AppointmentController:

    # [GET] /components
    def index(self):
        return render_template("appointment.html", page="Đặt lịch sửa xe")
