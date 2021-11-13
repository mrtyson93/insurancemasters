from flask import Blueprint, render_template

stateselection = Blueprint(
    'stateselection', __name__, template_folder='templates')

@stateselection.route("/state-selection")
def stateselection_load():

    return render_template('state-selection.html')
