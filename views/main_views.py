from flask import Blueprint

bp = Blueprint("main",__name__, url_prefix='/')

@bp.route("/")
def hello():
    return f'Hello, {__name__}'

@bp.route("/soom")
def hello_soom():
    return f'Hello, soom'