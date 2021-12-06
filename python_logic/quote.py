DO_NOT_INSURE = 0
BASE_QUOTE = 99

class InsuranceQuote(object):

    def __init__(self, questions):
        self.questions = questions

    def set_questions(self, questions):
        self.questions = questions

    def render_quote(self):
        factor = 1
        for question in self.questions:
            if question.structure_name == "BUSINESS_SCTRUCTURES":
                if question.value == "soleproprietorship":
                    question.factor = 1.5
                elif question.value == "llc":
                    question.factor = 1
                else:
                    question.factor = 2
            if question.structure_name == "BUSINESS_AGES":
                if question.value == "0.5":
                    question.factor = 1.5
                elif question.value == "5":
                    question.factor = 1.2
                elif question.value == "20":
                    question.factor = 1.1
                else:
                    question.factor = 1
            if question.structure_name == "EMPLOYEE_COUNTS":
                if question.value == "1":
                    question.factor = 1
                elif question.value == "5":
                    question.factor = 1.1
                elif question.value == "25":
                    question.factor = 1.2
                else:
                    question.factor = DO_NOT_INSURE  # we do not insure
            if question.structure_name == "REVENUES":
                if question.value == "1":
                    question.factor = 1
                elif question.value == "10":
                    question.factor = 1.05
                elif question.value == "100":
                    question.factor = 1.1
                elif question.value == "1000":
                    question.factor = 1.15
                else:
                    question.factor = DO_NOT_INSURE  # we do not insure
            if question.structure_name == "BUSINESS_NATURES":
                if question.value == "1":
                    question.factor = 1.1
                elif question.value == "2":
                    question.factor = 0.7
                elif question.value == "3":
                    question.factor = 0.9
                elif question.value == "4":
                    question.factor = 0.8
                else:
                    question.factor = 1
            if question.structure_name == "DEDUCTIBLE_OPTIONS":
                if question.value == "1":
                    question.factor = 1
                elif question.value == "2":
                    question.factor = 0.9
                elif question.value == "3":
                    question.factor = 0.8
                else:
                    question.factor = 0.75
            if question.structure_name == "COVERAGE_PER_INCIDENT_OPTIONS":
                if question.value == "1":
                    question.factor = 1
                elif question.value == "2":
                    question.factor = 0.9
                else:
                    question.factor = 0.75
            factor *= question.factor
        return factor * BASE_QUOTE
class Question:
    def __init__(self, structure_name, value, factor):
        self.structure_name = structure_name
        self.value = value
        self.factor = factor

    def __repr__(self):
        return "%s, %s, %s" % (self.structure_name, self.value, self.factor)
