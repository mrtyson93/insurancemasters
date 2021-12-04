from flask import Blueprint, render_template, request, session
from .helper import *

quotebusiness = Blueprint(
    'quotebusiness', __name__, template_folder='templates')

BUSINESS_SCTRUCTURES = [
  {"value": "soleproprietorship", "text": "Sole Proprietorship", "selected": "yes"},
  {"value": "llc", "text": "LLC", "selected": "no"},
  {"value": "corporate", "text": "Corporate", "selected": "no"},
]

BUSINESS_AGES = [
  {"value": "0.5", "text": "Less than a year", "selected": "yes"},
  {"value": "5", "text": "1-5 Years", "selected": "no"},
  {"value": "20", "text": "6-20 Years", "selected": "no"},
  {"value": "25", "text": "20+ Years", "selected": "no"},
]

EMPLOYEE_COUNTS = [
  {"value": "1", "text": "1", "selected": "yes"},
  {"value": "5", "text": "2-5", "selected": "no"},
  {"value": "25", "text": "6-25", "selected": "no"},
  # {"value": "50", "text": "25+"},
]

REVENUES = [
  {"value": "1", "text": "Less than $250k/yr", "selected": "yes"},
  {"value": "10", "text": "Between $250k/yr and $1M/yr", "selected": "no"},
  {"value": "100", "text": "$1M-$5M", "selected": "no"},
  {"value": "1000", "text": "$5M-$25M", "selected": "no"},
  # {"value": "10000", "text": "$25M+"},
]

LAST_YEAR_REVENUES = [
  {"value": "1", "text": "Less than $250k/yr", "selected": "yes"},
  {"value": "10", "text": "Between $250k/yr and $1M/yr", "selected": "no"},
  {"value": "100", "text": "$1M-$5M", "selected": "no"},
  {"value": "1000", "text": "$5M-$25M", "selected": "no"},
  # {"value": "10000", "text": "$25M+"},
]

BUSINESS_NATURES = [  
  {"value": "1", "text": "Manufacture, distribute, construct, install, or repair tangible goods", "selected": "yes"},
  {"value": "2", "text": "Sales or business development", "selected": "no"},
  {"value": "3", "text": "Consult in agriculture, medical, aerospace, environmental, oil/gas", "selected": "no"},
  {"value": "4", "text": "Consult in technology, management, legal, education, and associated training", "selected": "no"},
  {"value": "other", "text": "Other", "selected": "no"},
]




@quotebusiness.route("/quoteaboutbusiness", methods=['POST', 'GET'])
def quotebusiness_load():
    global BUSINESS_SCTRUCTURES, BUSINESS_AGES, EMPLOYEE_COUNTS, LAST_YEAR_REVENUES, REVENUES, BUSINESS_NATURES
    # set default form value
    startpicker_value = ""
    business_natures_other=""
    show_other = False
    if request.method == 'POST':
        first_name = request.form['txt-field-first-name']
        session['first_name'] = first_name.strip()
        last_name = request.form['txt-field-last-name']
        session['last_name'] = last_name.strip()
        business_name = request.form['txt-field-business-name']
        session['business_name'] = business_name.strip()
        firm_dba = request.form['txt-field-firm-dba']
        session['firm_dba'] = firm_dba.strip()
        former_name = request.form['txt-field-former-name']
        session['former_name'] = former_name.strip()
        phone_number = request.form['txt-field-phone']
        session['phone_number'] = phone_number.strip()
        email = request.form['txt-field-email']
        session['email'] = email.strip()
        business_address = request.form['txt-field-address']
        session['business_address'] = business_address.strip()
        business_city = request.form['txt-field-city']
        session['business_city'] = business_city.strip()
        business_state = request.form['select-field-state']
        session['business_state'] = business_state.strip()
        business_zip = request.form['txt-field-zip']
        session['business_zip'] = business_zip.strip()



    if 'business_structures' in session:
        BUSINESS_SCTRUCTURES = Helper.change_selected_options(BUSINESS_SCTRUCTURES, session['business_structures'])
    if 'business_ages' in session:
        BUSINESS_AGES = Helper.change_selected_options(BUSINESS_AGES, session['business_ages'])
    if 'employee_counts' in session:
        EMPLOYEE_COUNTS = Helper.change_selected_options(EMPLOYEE_COUNTS, session['employee_counts'])
    if 'revenues_last_year' in session:
        LAST_YEAR_REVENUES = Helper.change_selected_options(LAST_YEAR_REVENUES, session['revenues_last_year'])
    if 'revenues' in session:
        REVENUES = Helper.change_selected_options(REVENUES, session['revenues'])
    if 'business_natures' in session:
        BUSINESS_NATURES = Helper.change_selected_options(BUSINESS_NATURES, session['business_natures'])
    if 'business_natures_other' in session:
        business_natures_other = session['business_natures_other']
    if len(business_natures_other) > 0 and session['business_natures'] == "other":
        show_other = True
    if 'coverage_start_date' in session:
        startpicker_value = session['coverage_start_date']


    return render_template('quotebusiness.html', BUSINESS_SCTRUCTURES=BUSINESS_SCTRUCTURES, BUSINESS_AGES=BUSINESS_AGES,
                           EMPLOYEE_COUNTS=EMPLOYEE_COUNTS, LAST_YEAR_REVENUES=LAST_YEAR_REVENUES, REVENUES=REVENUES,
                           BUSINESS_NATURES=BUSINESS_NATURES,
                           business_natures_other=business_natures_other,
                           show_other=show_other,
                           coverage_start_date=startpicker_value)

