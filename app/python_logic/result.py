from flask import Blueprint, render_template

result = Blueprint(
    'result', __name__, template_folder='templates')

@result.route("/result", methods=['POST'])
def result_load():

    return render_template('result.html')
