from flask import Blueprint, render_template

about = Blueprint(
    'about', __name__, template_folder='templates')

@about.route("/about")
def about_load():

    return render_template('about.html')
