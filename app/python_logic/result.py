import locale

from flask import Blueprint, render_template, request
from .quote import Question, InsuranceQuote
from .quoteBusiness import DEDUCTIBLE_OPTIONS, COVERAGE_PER_INCIDENT_OPTIONS


BASE_QUOTE = 99

locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')

result = Blueprint(
    'result', __name__, template_folder='templates')


def format_currency(value):
    return locale.currency(value, symbol=True, grouping=True)


@result.route("/result", methods=['POST'])
def result_load():
    # TODO add business logic here
    your_quote = BASE_QUOTE
    questions = []
    # BUSINESS_SCTRUCTURES
    business_structure_value = request.form['business_structures']
    questions.append(Question("BUSINESS_SCTRUCTURES", business_structure_value, 1))
    # BUSINESS_AGES
    business_ages_value = request.form['business_ages']
    questions.append(Question("BUSINESS_AGES", business_ages_value, 1))
    # EMPLOYEE_COUNTS
    employee_counts_value = request.form['employee_counts']
    questions.append(Question("EMPLOYEE_COUNTS", employee_counts_value, 1))
    # REVENUES
    revenues_value = request.form['revenues']
    questions.append(Question("REVENUES", revenues_value, 1))
    # BUSINESS_NATURES
    business_natures_value = request.form['business_natures']
    questions.append(Question("BUSINESS_NATURES", business_natures_value, 1))

    quote = InsuranceQuote(questions)
    quote.render_quote()
    for q in questions:
        your_quote *= q.factor

    return render_template('result.html', display_quote=format_currency(your_quote), quote=your_quote, DEDUCTIBLE_OPTIONS=DEDUCTIBLE_OPTIONS, COVERAGE_PER_INCIDENT_OPTIONS=COVERAGE_PER_INCIDENT_OPTIONS)




