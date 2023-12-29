""" ROUTES FOR MAIN """
#pylint: disable=E0401
from flask import (
    render_template,
    Blueprint,
    request,
)

from flask_login import(
    current_user
)

from markupsafe import Markup


main_blueprint= Blueprint(
    "main",
    __name__,
    template_folder="templates",
)

@main_blueprint.route('/')
def welcome():
    """ HOME PAGE """
    user_name = get_username()
    svg = svg_github()
    return render_template('home.jinja2', user_name=user_name, svg=Markup(svg))

@main_blueprint.route('/navbar_layout')
def navbar_layout():
    """ DYNAMIC MENU """
    layout_type = request.args.get('layout', 'default')
    current = request.args.get('current', '/')
    if layout_type == 'account':
        #List of dictionaries for acount-sepecific links
        return render_template('nav_account.jinja2', current=current)
    if layout_type == 'blog':
        #List of dictionaries for acount-sepecific links
        return render_template('nav_blog.jinja2', current=current)

    # List of dictionaries for default links
    return render_template('nav_default.jinja2', current=current)

@main_blueprint.route('/nav_mobile')
def nav_mobile():
    """ DYNAMIC NAVBAR """
    current = request.args.get('current', '/')
    layout_type = request.args.get('layout', 'default')
    print(f"Current: {current} Route: nav_bar")
    if layout_type == '/blog':
        #List of dictionaries for acount-sepecific links
        return render_template('nav_blog_mobile.jinja2', current=current)
    # List of dictionaries for default links
    return render_template('nav_mobile.jinja2', current=current)

@main_blueprint.route('/mobile_close')
def mobile_close():
    """ DYNAMIC NAVBAR """
    current = request.args.get('current', '/')
    print(f"Current: {current} Route: mobile_close")
    return render_template('nav_close_mobile.jinja2', current=current)


@main_blueprint.route('/projects')
def project():
    """ DYNAMIC DISPLAY """
    user_name = get_username()
    svg = svg_github()
    return render_template('projects.jinja2', user_name=user_name, svg=svg)


@main_blueprint.route('/about')
def about():
    """ DYNAMIC DISPLAY """
    user_name = get_username()
    svg = svg_github()
    return render_template('about.jinja2', user_name=user_name, svg=svg)

@main_blueprint.route('/blog')
def blog():
    """ DYNAMIC DISPLAY """
    user_name = get_username()
    svg = svg_github()
    is_authenticated = current_user.is_authenticated
    return render_template('blog.jinja2', user_name=user_name, svg=svg, is_authenticated=is_authenticated)

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
