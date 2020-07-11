from flask import Blueprint, render_template


route_blueprint = Blueprint('routes', __name__)


@route_blueprint.route('/', methods=['GET'])
def landing_page():
    return render_template('landing_page.html')
