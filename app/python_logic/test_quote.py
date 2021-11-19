import unittest

from quote import Question, Quote, DO_NOT_INSURE


class TestQuote(unittest.TestCase):
    def test_business_structure_sole_proprietorship(self):
        questions = [Question("BUSINESS_SCTRUCTURES", "soleproprietorship", 1)]
        quote = Quote(questions)
        quote.render_quote()
        self.assertEqual(1.5, questions[0].factor)

    def test_business_structure_llc(self):
        questions = [Question("BUSINESS_SCTRUCTURES", "llc", 1)]
        quote = Quote(questions)
        quote.render_quote()
        self.assertEqual(1, questions[0].factor)

    def test_business_structure_corporate(self):
        questions = [Question("BUSINESS_SCTRUCTURES", "corporate", 1)]
        quote = Quote(questions)
        quote.render_quote()
        self.assertEqual(2, questions[0].factor)

    def test_business_age_less_than_a_year(self):
        questions = [Question("BUSINESS_AGES", "0.5", 1)]
        quote = Quote(questions)
        quote.render_quote()
        self.assertEqual(1.5, questions[0].factor)

    def test_business_age_1_to_5_years(self):
        questions = [Question("BUSINESS_AGES", "5", 1)]
        quote = Quote(questions)
        quote.render_quote()
        self.assertEqual(1.2, questions[0].factor)

    def test_business_age_6_to_20_years(self):
        questions = [Question("BUSINESS_AGES", "20", 1)]
        quote = Quote(questions)
        quote.render_quote()
        self.assertEqual(1.1, questions[0].factor)

    def test_business_age_20_plus_years(self):
        questions = [Question("BUSINESS_AGES", "25", 1)]
        quote = Quote(questions)
        quote.render_quote()
        self.assertEqual(1, questions[0].factor)

    def test_employee_counts_1(self):
        questions = [Question("EMPLOYEE_COUNTS", "1", 1)]
        quote = Quote(questions)
        quote.render_quote()
        self.assertEqual(1, questions[0].factor)

    def test_employee_counts_2_to_5(self):
        questions = [Question("EMPLOYEE_COUNTS", "5", 1)]
        quote = Quote(questions)
        quote.render_quote()
        self.assertEqual(1.1, questions[0].factor)

    def test_employee_counts_6_to_25(self):
        questions = [Question("EMPLOYEE_COUNTS", "25", 1)]
        quote = Quote(questions)
        quote.render_quote()
        self.assertEqual(1.2, questions[0].factor)

    def test_employee_counts_25_plus(self):
        questions = [Question("EMPLOYEE_COUNTS", "50", 1)]
        quote = Quote(questions)
        quote.render_quote()
        self.assertEqual(DO_NOT_INSURE, questions[0].factor)
