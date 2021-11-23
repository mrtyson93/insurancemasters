from flask import Blueprint, render_template, request

quoteyou = Blueprint(
    'quoteyou', __name__, template_folder='templates')


@quoteyou.route("/quoteaboutyou", methods=['POST'])
def quoteyou_load():
    selected_state = request.form['select-state-dropdown']
    return render_template('quoteyou.html', selected_state=selected_state)
