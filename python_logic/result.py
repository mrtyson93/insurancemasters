

from flask import Blueprint, render_template, request, session
from .quote import Question, InsuranceQuote
from .quoteBusiness import *
from .helper import *

DEDUCTIBLE_OPTIONS = [
  {"value": "1", "text": "Default $0", "selected": "yes"},
  {"value": "2", "text": "$2,500", "selected": "no"},
  {"value": "3", "text": "$5,000", "selected": "no"},
  {"value": "4", "text": "$10,000", "selected": "no"},
]

COVERAGE_PER_INCIDENT_OPTIONS = [
  {"value": "1", "text": "Default $1M", "selected": "yes"},
  {"value": "2", "text": "$500K", "selected": "no"},
  {"value": "3", "text": "$250K", "selected": "no"},
]


result = Blueprint(
    'result', __name__, template_folder='templates')





@result.route("/result", methods=['POST', 'GET'])
def result_load():
    # TODO add business logic here
    # default selection values
    global DEDUCTIBLE_OPTIONS, COVERAGE_PER_INCIDENT_OPTIONS
    questions = []
    business_structure_value = "soleproprietorship"
    business_ages_value = "0.5"
    employee_counts_value = "1"
    revenues_value = "1"
    business_natures_value = "1"
    deductible_options_value = "1"
    coverage_per_incident_options_value = "1"

    if request.method == 'POST':
        # BUSINESS_SCTRUCTURES
        business_structure_value = request.form['business_structures']
        session['business_structures'] = business_structure_value
        # BUSINESS_AGES
        business_ages_value = request.form['business_ages']
        session['business_ages'] = business_ages_value
        # EMPLOYEE_COUNTS
        employee_counts_value = request.form['employee_counts']
        session['employee_counts'] = employee_counts_value
        # REVENUES
        revenues_value = request.form['revenues']
        session['revenues'] = revenues_value
        # LAST YEAR REVENUES
        revenues_last_year_value = request.form['revenues_last_year']
        session['revenues_last_year'] = revenues_last_year_value
        # BUSINESS_NATURES
        business_natures_value = request.form['business_natures']
        session['business_natures'] = business_natures_value
        session['business_natures_other'] = request.form['txt-field-other-business-nature']
        # Coverage Start Date
        startpicker_value = request.form['startpicker']
        session['coverage_start_date'] = startpicker_value
    else:
        if 'business_structures' in session:
            business_structure_value = session['business_structures']
        if 'business_ages' in session:
            business_ages_value = session['business_ages']
        if 'employee_counts' in session:
            employee_counts_value = session['employee_counts']
        if 'revenues' in session:
            revenues_value = session['revenues']
        if 'business_natures' in session:
            business_natures_value = session['business_natures']

    if 'deductible_options' in session:
        DEDUCTIBLE_OPTIONS = Helper.change_selected_options(DEDUCTIBLE_OPTIONS, session['deductible_options'])
        deductible_options_value = session['deductible_options']
    if 'coverage_per_incident_options' in session:
        COVERAGE_PER_INCIDENT_OPTIONS = Helper.change_selected_options(COVERAGE_PER_INCIDENT_OPTIONS,
                                                                       session['coverage_per_incident_options'])
        coverage_per_incident_options_value = session['coverage_per_incident_options']

    questions.append(Question("BUSINESS_SCTRUCTURES", business_structure_value, 1))
    questions.append(Question("BUSINESS_AGES", business_ages_value, 1))
    questions.append(Question("EMPLOYEE_COUNTS", employee_counts_value, 1))
    questions.append(Question("REVENUES", revenues_value, 1))
    questions.append(Question("BUSINESS_NATURES", business_natures_value, 1))

    quote = InsuranceQuote(questions)
    your_quote = quote.render_quote()

    questions.append(Question("DEDUCTIBLE_OPTIONS", deductible_options_value, 1))
    questions.append(Question("COVERAGE_PER_INCIDENT_OPTIONS", coverage_per_incident_options_value, 1))
    quote = InsuranceQuote(questions)
    final_quote = quote.render_quote()

    return render_template('result.html', display_quote=Helper.format_currency(final_quote),
                           quote=your_quote,
                           DEDUCTIBLE_OPTIONS=DEDUCTIBLE_OPTIONS,
                           COVERAGE_PER_INCIDENT_OPTIONS=COVERAGE_PER_INCIDENT_OPTIONS,
                           final_quote=final_quote)




