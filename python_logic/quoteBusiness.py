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
  {"value": "0.5", "text": "Less than a year"},
  {"value": "5", "text": "1-5 Years"},
  {"value": "20", "text": "6-20 Years"},
  {"value": "25", "text": "20+ Years"},
]

EMPLOYEE_COUNTS = [
  {"value": "1", "text": "1"},
  {"value": "5", "text": "2-5"},
  {"value": "25", "text": "6-25"},
  # {"value": "50", "text": "25+"},
]

REVENUES = [
  {"value": "1", "text": "Less than $250k/yr"},
  {"value": "10", "text": "Between $250k/yr and $1M/yr"},
  {"value": "100", "text": "$1M-$5M"},
  {"value": "1000", "text": "$5M-$25M"},
  # {"value": "10000", "text": "$25M+"},
]

BUSINESS_NATURES = [  
  {"value": "1", "text": "Manufacture, distribute, construct, install, or repair tangible goods"},
  {"value": "2", "text": "Sales or business development"},
  {"value": "3", "text": "Consult in agriculture, medical, aerospace, environmental, oil/gas"},
  {"value": "4", "text": "Consult in technology, management, legal, education, and associated training"},
  {"value": "other", "text": "Other"},
]

DEDUCTIBLE_OPTIONS = [
  {"value": "1", "text": "Default $0"},
  {"value": "2", "text": "$2,500"},
  {"value": "3", "text": "$5,000"},
  {"value": "4", "text": "$10,000"},
]

COVERAGE_PER_INCIDENT_OPTIONS = [
  {"value": "1", "text": "Default $1M"},
  {"value": "2", "text": "$500K"},
  {"value": "3", "text": "$250K"},
]


@quotebusiness.route("/quoteaboutbusiness", methods=['POST', 'GET'])
def quotebusiness_load():
    global BUSINESS_SCTRUCTURES
    if request.method == 'POST':
        session['business_name'] = request.form['txt-field-business-name']

    if 'business_structures' in session:
        BUSINESS_SCTRUCTURES = Helper.change_selected_options(BUSINESS_SCTRUCTURES, session['business_structures'])

    return render_template('quotebusiness.html', BUSINESS_SCTRUCTURES=BUSINESS_SCTRUCTURES, BUSINESS_AGES=BUSINESS_AGES,
                           EMPLOYEE_COUNTS=EMPLOYEE_COUNTS, REVENUES=REVENUES, BUSINESS_NATURES=BUSINESS_NATURES,
                           bs=session['business_structures'])

