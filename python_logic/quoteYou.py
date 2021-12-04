from flask import Blueprint, render_template, request, session

quoteyou = Blueprint(
    'quoteyou', __name__, template_folder='templates')


@quoteyou.route("/quoteaboutyou", methods=['POST', 'GET'])
def quoteyou_load():
    # default form entry
    selected_state = 'CA'
    business_name = ""
    first_name = ""
    last_name = ""
    firm_dba = ""
    former_name = ""
    phone_number = ""
    email = ""
    business_address = ""
    business_city = ""
    business_state = ""
    business_zip = ""
    if request.method == 'POST':
        selected_state = request.form['select-state-dropdown']
        session['insured_state'] = selected_state.strip()

    if 'insured_state' in session:
        selected_state = session['insured_state']
    if 'first_name' in session:
        first_name = session['first_name']
    if 'last_name' in session:
        last_name = session['last_name']
    if 'business_name' in session:
        business_name = session['business_name']
    if 'firm_dba' in session:
        firm_dba = session['firm_dba']
    if 'former_name' in session:
        former_name = session['former_name']
    if 'phone_number' in session:
        phone_number = session['phone_number']
    if 'email' in session:
        email = session['email']
    if 'business_address' in session:
        business_address = session['business_address']
    if 'business_city' in session:
        business_city = session['business_city']
    if 'business_state' in session:
        selected_state = session['business_state']
    if 'business_zip' in session:
        business_zip = session['business_zip']

    return render_template('quoteyou.html', first_name=first_name, last_name=last_name,
                           business_name=business_name, firm_dba=firm_dba, former_name=former_name,
                           phone_number=phone_number, email=email, business_address=business_address,
                           business_city=business_city, selected_state=selected_state, business_zip=business_zip)
