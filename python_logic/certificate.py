from flask import Blueprint, render_template, session
from datetime import datetime

certificate = Blueprint(
    'certificate', __name__, template_folder='templates')

@certificate.route("/certificate")
def certificate_load():
    #default value
    business_name = ""
    insured_state = ""
    coverage_start_date = ""
    if 'business_name' in session:
        business_name = session['business_name']
    if 'insured_state' in session:
        insured_state = session['insured_state']
        if insured_state == "CA":
            insured_state = "California"
        if insured_state == "WA":
            insured_state = "Washington"
        if insured_state == "VA":
            insured_state = "Virginia"
        if insured_state == "FL":
            insured_state = "Florida"
        if insured_state == "TX":
            insured_state = "Texas"
    if 'coverage_start_date' in session:
        coverage_start_date = session['coverage_start_date']

    now = datetime.now()
    return render_template('certificate.html', business_name=business_name, insured_state=insured_state,
                           coverage_start_date=coverage_start_date, issue_date=now.strftime("%m/%d/%Y"))

