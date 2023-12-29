""" COMPILE STATIC ASSESTS """
from flask import Flask
from flask_assets import Bundle, Environment


def compile_static_assets(app: Flask):
    """ COMPILE ALL ASSET BUNDLES AT TOP LEVEL """
    assets = Environment(app)
    compile_javascript(assets, app)
    compile_stylesheets(assets, app)
    #compile_auth_stylesheets(assets, app)

#-------------------------------Home------------------------------------#

def compile_stylesheets(assets: Environment, app: Flask):
    """Compile Tailwind CSS."""

    css = Bundle("dist/css/main.css", output="dist/css/main.min.css")

    assets.register("css", css)

    # Build assets in development mode
    if app.config['ENVIRONMENT'] != 'production':
        with app.app_context():
            css.build(force=True)




def compile_javascript(assets: Environment, app: Flask):
    """ BUNDLE AND BUILD JS FILES """

    # JavaScript Bundle
    js_bundle_main = Bundle(
        "src/js/alert.js",
        "dist/js/htmx.min.js",
        filters="jsmin", output="dist/js/home.min.js")

    # Register assets
    assets.register("js_home", js_bundle_main)


    # Build assets in development mode
    if app.config['ENVIRONMENT'] != 'production':
        with app.app_context():
            js_bundle_main.build(force=True)
