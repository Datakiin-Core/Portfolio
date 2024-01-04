""" ROUTES FOR AUTHENTICATION """
from typing import Optional
#pylint: disable=E0401
from flask import (
    Blueprint,
    Response,
    flash,
    redirect,
    render_template,
    request,
    url_for
    )

from flask_login import (
    current_user,
    login_user,
    logout_user
    )

from app.forms import LoginForm, SignupForm, UpdateForm
from app.models import User, db
from app import login_manager

auth_blueprint = Blueprint(
    "auth",
    __name__,
    template_folder="templates"
)


@auth_blueprint.route("/signup", methods=["GET", "POST"])
def signup() -> Response:
    """ 
    VIEW FOR NEW USERS TO SIGN UP

    GET: Serve sign-up page.
    POST: Validate form, create account, redirect user to home
    """
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.user_email.data).first()
        if existing_user is None:
            user = User(name=form.user_name.data,
                        email=form.user_email.data,
                        website=form.user_metadata_website.data)
            user.set_password(form.user_password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            print(user)
            return redirect('/blog')
        flash("A user already exists with that email address.")

    return render_template(
        "auth_signup.jinja2",
        title="Create an Account.",
        form=form,
        template="signup-page",
        body="Sign up for a user account.",
    )



@auth_blueprint.route("/update", methods=["GET", "POST"])
def update() -> Response:
    """ 
    VIEW FOR USERS TO UPDATE PASSWORD

    GET: Serve Update page.
    POST: Validate form, update password, redirect user to home
    """
    form = UpdateForm()
    extension = request.args.get('extension', 'home_layout.jinja2')
    if form.validate_on_submit():
        if current_user.is_authenticated:
            print("Setting User")
            user = current_user
            print(user)
            print(user.check_password(password=form.old_user_password.data))
            if user.check_password(password=form.old_user_password.data):
                print("Password Check")
                user.set_password(form.user_password.data)
                db.session.add(user)
                db.session.commit()
                return redirect('/blog')
        flash("Invalid credentials or user not logged in.")

    return render_template(
        "auth_update.jinja2",
        title="Update Password.",
        form=form,
        template="upate-page",
        body="Update Password.",
        extension=extension,
    )

@auth_blueprint.route('/login', methods=["GET", "POST"])
def login() -> Response:
    """
    LOG-IN PAGE

    GET: Serve Log-in page.
    POST: Validate form and redirect user to home.

    :returns: Response
    """
    # Redirect authenticated users to the home page
    if current_user.is_authenticated:
        print(f"Redirect: {current_user.is_authenticated}")
        return redirect('/')

    form = LoginForm()
    next_path = request.args.get('path', '')  # Fetch path from query parameter

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.user_email.data).first()
        if user and user.check_password(password=form.user_password.data):
            login_user(user)
            return redirect(form.next.data or '/')

        flash("Invalid username/password combination")

    # Set the next field only on GET request
    if request.method == 'GET':
        form.next.data = next_path

    return render_template(
        "auth_login.jinja2",
        form=form,
        title="Log In",
        template="login-page",
        body="Log in with your User account.",
        next_path=next_path
    )


@auth_blueprint.route("/logout", methods=["GET"])
def logout() -> Response:
    """
    LOG-OUT
    """
    if current_user.is_authenticated:
        logout_user()

    return redirect('/')

@login_manager.user_loader
def load_user(user_id: int) -> Optional[User]:
    """ CHECK IF LOGGED IN """
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized() -> Response:
    """ REDIRECT TO LOGIN """
    flash("You must be logged in to view that page.")
    return redirect(url_for("auth.login"))
