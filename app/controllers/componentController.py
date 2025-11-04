from flask import Flask, render_template


class ComponentController:

    # [GET] /components
    def index(self):
        return render_template("components.html")
    

    # [GET] /components/:slug
    def show(self,slug):
        return render_template("components.html",slug=slug)
