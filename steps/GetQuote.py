from behave import *

from python_logic.quote import Question,InsuranceQuote

DEFAULT_QUOTE_OPTIONS = {
  "BUSINESS_SCTRUCTURES": "soleproprietorship",
  "BUSINESS_AGES": "0.5",
  "EMPLOYEE_COUNTS":  "1",
  "REVENUES": "1",
  "BUSINESS_NATURES": "1",
  "DEDUCTIBLE_OPTIONS": "1",
  "COVERAGE_PER_INCIDENT_OPTIONS": "1"
}

@given('I am a small business owner')
def step_impl(context):
  #initialize quote for user
  context.quote = InsuranceQuote([])
  assert type(context.quote) == type(InsuranceQuote([]))

@when('I choose the default coverage options')
def step_impl(context):
  #construct all questions to be passed into quote
  questions = [Question(option, choice, 1) for option, choice in DEFAULT_QUOTE_OPTIONS.items()]
  context.quote.set_questions(questions)
  #assert quote has 7 questions
  assert len(context.quote.questions) == 7
  #assert questions[0] is actually a question
  assert type(context.quote.questions[0]) == type(Question("BUSINESS_AGES",1,1))

@when('I choose to See Quote')
def step_impl(context):
    context.final_quote = context.quote.render_quote()
    #assert final quote is a floar
    assert type(context.final_quote) == float

@then('I get a quote of "{expected_quote_result}"')
def step_impl(context, expected_quote_result):
    #assert computed quote is equal to expected quote
    assert context.final_quote == float(expected_quote_result)

