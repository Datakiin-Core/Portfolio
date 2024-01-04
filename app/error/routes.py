""" ROUTES FOR BLOG """
#pylint: disable=E0401
from flask import (
    render_template,
    Blueprint,
    request,
)

error_blueprint = Blueprint(
    "error",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@error_blueprint.errorhandler(404)
def page_not_found(e):
    # You can use a different template for 404 errors if you prefer
    return render_template('404.jinja2'), 404

@error_blueprint.route('/error', methods=['GET', 'POST'])
def error():
    """ DYNAMIC DISPLAY """
    error_message = "An unexpected error occurred."
    if request.args.get('error_message'):
        error_message = request.args.get('error_message')
    return render_template('error.jinja2', error_message=error_message)

