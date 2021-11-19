DO_NOT_INSURE = 10000


class Quote(object):

    def __init__(self, questions):
        self.questions = questions

    def render_quote(self):
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
                    question.factor = DO_NOT_INSURE # we do not insure, so use


class Question:
    def __init__(self, structure_name, value, factor):
        self.structure_name = structure_name
        self.value = value
        self.factor = factor

    def __repr__(self):
        return "%s, %s, %s" % (self.structure_name, self.value, self.factor)
