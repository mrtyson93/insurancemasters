from flask import Blueprint, render_template, request, session

quoteyou = Blueprint(
    'quoteyou', __name__, template_folder='templates')


@quoteyou.route("/quoteaboutyou", methods=['POST', 'GET'])
def quoteyou_load():
    if request.method == 'POST':
        selected_state = request.form['select-state-dropdown']
        session['insured_state'] = selected_state.strip()

    if 'insured_state' in session:
        selected_state = session['insured_state']

    if 'business_name' in session:
        business_name = session['business_name']

    return render_template('quoteyou.html', selected_state=selected_state, business_name=business_name)
