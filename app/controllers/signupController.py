from flask import Flask, render_template


class SignupController:
    # [GET] /signup
    def index(self):
        return render_template("register_login.html", page="account")

