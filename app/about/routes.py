""" ROUTES FOR BLOG """
#pylint: disable=E0401
from flask import (
    render_template,
    Blueprint,
    request,
    url_for,
    session
)

from flask_login import(
    current_user
)

about_blueprint= Blueprint(
    "about",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@about_blueprint.route('/about', methods=['GET', 'POST'])
def about():
    """ DYNAMIC DISPLAY """
    print(f"This is {request.path}")
    is_authenticated = current_user.is_authenticated
    missing_img = url_for('static', filename='src/images/missing_img.svg')
    return render_template('about.jinja2',
                           is_authenticated=is_authenticated,
                           missing_img=missing_img)

@about_blueprint.before_request
def track_history():
    if 'history' not in session:
        session['history'] = []
    session['history'].append(request.url)
    if len(session['history']) > 10:  # Limit history length
        session['history'].pop(0)

def get_username():
    """ Get Username """
    if current_user.is_authenticated:
        user_name = current_user.name
    else:
        user_name = "Guest"

    return user_name

def svg_github():
    """ DYNAMIC MENU """
    with open('app/home/img/github.svg', 'r',  encoding="utf-8") as file:
        svg = file.read()

    return svg
