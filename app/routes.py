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

from .data_assets import(MenuAsset)

main_blueprint= Blueprint(
    "main",
    __name__,
    template_folder="templates",
)

# links
home         = MenuAsset(name="Home"     ,links="/")
about        = MenuAsset(name="About"    ,links="/about")
projects     = MenuAsset(name="Projects" ,links="/projects")
blog         = MenuAsset(name="Blog"     ,links="/blog")
feed         = MenuAsset(name="Feed"     ,links="/feed")
login        = MenuAsset(name="Login"    ,links="/login")
logout       = MenuAsset(name="Logout"   ,links="/logout")
signup       = MenuAsset(name="Signup"   ,links="/signup")
password     = MenuAsset(name="Password" ,links="/update")
user         = MenuAsset(name="User Menu",links="close")
close        = MenuAsset(name="Close"    ,links="user")
exit_project = MenuAsset(name="Exit"     ,links="/projects")

default_menu = []

@main_blueprint.route('/layout')
def layout():
    """ DYNAMIC MENU """

    next_page = request.args.get('next_page', "/feed")
    print(next_page)
    next = MenuAsset(name="Exit"     ,links="/feed")
    menu = request.args.get('menu', 'default')
    is_authenticated = current_user.is_authenticated
    menu_links = []
    if menu == 'default':
        menu_links = [home, about, projects]
    if menu == 'blog':
        menu_links = [feed, blog, exit_project]
    if menu == 'user_menu':
        if is_authenticated:
            menu_links = [logout, password]
        else:
            menu_links = [login, signup]


    return render_template('nav_portfolio.jinja2',
                            is_authenticated=is_authenticated, menu_links=menu_links, next=next)


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
