from flask import render_template, request
from ..controller import controller


@controller.route((''))
def home():
    return render_template("dist/index.html")
