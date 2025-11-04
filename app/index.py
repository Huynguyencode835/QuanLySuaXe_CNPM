from flask import Flask, render_template
from flask.views import View
from routes.index import route

app = Flask(__name__)

route(app)

if __name__ == "__main__":
    app.run(debug=True)