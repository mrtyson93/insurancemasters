from flask import Blueprint, render_template, request, session
from .helper import *
from .result import *

payment = Blueprint(
    'payment', __name__, template_folder='templates')


@payment.route("/payment", methods=['POST', 'GET'])
def payment_load():
    # load quote information
    business_name = "N/A"
    coverage_start_date = "N/A"
    final_quote = BASE_QUOTE
    deductible_options = "1"
    coverage_per_incident_options = "1"
    if request.method == 'POST':
        deductible_options_value = request.form['deductible_options']
        session['deductible_options'] = deductible_options_value
        coverage_per_incident_options_value = request.form['coverage_per_incident_options']
        session['coverage_per_incident_options'] = coverage_per_incident_options_value
        final_quote_value = request.form['final_quote_value']
        session['final_quote'] = final_quote_value

    if 'business_name' in session:
        business_name = session['business_name']
    if 'coverage_start_date' in session:
        coverage_start_date = session['coverage_start_date']
    if 'final_quote' in session:
        final_quote = session['final_quote']
    if 'deductible_options' in session:
        deductible_options = session['deductible_options']
    if 'coverage_per_incident_options' in session:
        coverage_per_incident_options = session['coverage_per_incident_options']

    display_deductible_options = DEDUCTIBLE_OPTIONS[int(deductible_options)-1]['text']
    display_coverage_per_incident_options = COVERAGE_PER_INCIDENT_OPTIONS[int(coverage_per_incident_options)-1]['text']
    return render_template('payment.html', business_name=business_name, coverage_start_date=coverage_start_date,
                           final_quote=Helper.format_currency(float(final_quote)), deductible_options=display_deductible_options,
                           coverage_per_incident_options=display_coverage_per_incident_options)

