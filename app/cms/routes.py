""" ROUTES FOR MAIN """
#pylint: disable=E0401
from flask import (
    render_template,
    Blueprint,
    flash
    
)

from flask_login import(
    current_user
)
from markupsafe import Markup
from app.blog_form import BlogPostForm




cms_blueprint= Blueprint(
    "cms",
    __name__,
    template_folder="templates",
)

@cms_blueprint.route('/cms')
def cms():
    """ / """
    user_name = get_username()
    return render_template('cms_blog.jinja2', user_name=user_name)

@cms_blueprint.route('/cms_home')
def home():
    """ HOME PAGE """
    user_name = get_username()
    return render_template('cms_home.jinja2', user_name=user_name)

@cms_blueprint.route('/cms_projects')
def projects():
    """ PROJECTS PAGE """
    user_name = get_username()
    return render_template('cms_projects.jinja2', user_name=user_name)

@cms_blueprint.route('/cms_about')
def about():
    """ ABOUT PAGE """
    user_name = get_username()
    svg = svg_github()
    return render_template('cms_about.jinja2', user_name=user_name, svg=Markup(svg))

@cms_blueprint.route('/cms_blog', methods=['GET', 'POST'])
def blog():
    """ BLOG PAGE """
    form = BlogPostForm()
    if form.validate_on_submit():
        # Process the submitted code
        flash('Code submitted successfully!')
        # With HTMX, you might return partial HTML here
    user_name = get_username()
    print(f"User Name: {user_name}")
    return render_template('cms_blog.jinja2', user_name=user_name, form=form)


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
