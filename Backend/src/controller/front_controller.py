from flask import render_template, request
from ..controller import controller


@controller.route((''))
def home():
    return render_template("dist/index.html")

# @controller.route('tarifas/api/', methods=['GET'], defaults={'path': ''})
# def home_api():
#     return render_template("dist/index.html")
