""" ROUTES FOR BLOG """
#pylint: disable=E0401
from flask import (
    render_template,
    Blueprint,
    flash,
    request,
    url_for

)

from flask_login import(
    current_user
)
from app.blog_form import BlogPostForm




blog_blueprint= Blueprint(
    "blog",
    __name__,
    template_folder="templates",
)

@blog_blueprint.route('/blog', methods=['GET', 'POST'])
def blog():
    """ BLOG PAGE """
    form = BlogPostForm()
    if form.validate_on_submit():
        # Process the submitted code
        flash('Code submitted successfully!')
        # With HTMX, you might return partial HTML here
    user_name = get_username()
    print(f"User Name: {user_name}")
    is_authenticated = current_user.is_authenticated
    print(f"Is Authenticated: {is_authenticated}")
    return render_template('blog.jinja2', user_name=user_name,
                            form=form,
                            is_authenticated=is_authenticated)

@blog_blueprint.route('/feed', methods=['GET', 'POST'])
def feed():
    """ DYNAMIC DISPLAY """
    next = "/blog"
    print(f"This is {request.path}")
    is_authenticated = current_user.is_authenticated
    missing_img = url_for('static', filename='src/images/missing_img.svg')
    return render_template('feed.jinja2',
                           is_authenticated=is_authenticated,
                           missing_img=missing_img,
                           next=next)


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
