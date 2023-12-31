""" ROUTES FOR BLOG """
#pylint: disable=E0401
from flask import (
    render_template,
    Blueprint,
    request,
    url_for
)

from flask_login import(
    current_user
)

projects_blueprint= Blueprint(
    "projects",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@projects_blueprint.route('/projects', methods=['GET', 'POST'])
def projects():
    """ DYNAMIC DISPLAY """
    print(f"This is {request.path}")
    is_authenticated = current_user.is_authenticated
    missing_img = url_for('static', filename='src/images/missing_img.svg')
    return render_template('projects.jinja2',
                           is_authenticated=is_authenticated,
                           missing_img=missing_img)


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
