import unittest

from .quote import Question, InsuranceQuote, DO_NOT_INSURE


class TestQuote(unittest.TestCase):
    def test_business_structure_sole_proprietorship(self):
        questions = [Question("BUSINESS_SCTRUCTURES", "soleproprietorship", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(99, questions[0].factor)

    def test_business_structure_llc(self):
        questions = [Question("BUSINESS_SCTRUCTURES", "llc", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1, questions[0].factor)

    def test_business_structure_corporate(self):
        questions = [Question("BUSINESS_SCTRUCTURES", "corporate", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(2, questions[0].factor)

    def test_business_age_less_than_a_year(self):
        questions = [Question("BUSINESS_AGES", "0.5", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1.5, questions[0].factor)

    def test_business_age_1_to_5_years(self):
        questions = [Question("BUSINESS_AGES", "5", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1.2, questions[0].factor)

    def test_business_age_6_to_20_years(self):
        questions = [Question("BUSINESS_AGES", "20", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1.1, questions[0].factor)

    def test_business_age_20_plus_years(self):
        questions = [Question("BUSINESS_AGES", "25", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1, questions[0].factor)

    def test_employee_counts_1(self):
        questions = [Question("EMPLOYEE_COUNTS", "1", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1, questions[0].factor)

    def test_employee_counts_2_to_5(self):
        questions = [Question("EMPLOYEE_COUNTS", "5", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1.1, questions[0].factor)

    def test_employee_counts_6_to_25(self):
        questions = [Question("EMPLOYEE_COUNTS", "25", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1.2, questions[0].factor)

    def test_revenues_less_than_250k(self):
        questions = [Question("REVENUES", "1", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1, questions[0].factor)

    def test_revenues_250k_to_1M(self):
        questions = [Question("REVENUES", "10", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1.05, questions[0].factor)

    def test_revenues_1M_to_5M(self):
        questions = [Question("REVENUES", "100", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1.1, questions[0].factor)

    def test_revenues_5M_to_25M(self):
        questions = [Question("REVENUES", "1000", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1.15, questions[0].factor)

    def test_business_nature_manufacture(self):
        questions = [Question("BUSINESS_NATURES", "1", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1.1, questions[0].factor)

    def test_business_nature_sales(self):
        questions = [Question("BUSINESS_NATURES", "2", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(0.7, questions[0].factor)

    def test_business_nature_agriculture(self):
        questions = [Question("BUSINESS_NATURES", "3", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(0.9, questions[0].factor)

    def test_business_nature_technology(self):
        questions = [Question("BUSINESS_NATURES", "4", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(0.8, questions[0].factor)

    def test_business_nature_other(self):
        questions = [Question("BUSINESS_NATURES", "other", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1, questions[0].factor)

    def test_deductible_options_default(self):
        questions = [Question("DEDUCTIBLE_OPTIONS", "1", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1, questions[0].factor)

    def test_deductible_options_2500(self):
        questions = [Question("DEDUCTIBLE_OPTIONS", "2", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(0.9, questions[0].factor)

    def test_deductible_options_5000(self):
        questions = [Question("DEDUCTIBLE_OPTIONS", "3", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(0.8, questions[0].factor)

    def test_deductible_options_10000(self):
        questions = [Question("DEDUCTIBLE_OPTIONS", "4", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(0.75, questions[0].factor)

    def test_coverage_per_incident_options_1M(self):
        questions = [Question("COVERAGE_PER_INCIDENT_OPTIONS", "1", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(1, questions[0].factor)

    def test_coverage_per_incident_options_500K(self):
        questions = [Question("COVERAGE_PER_INCIDENT_OPTIONS", "2", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(0.9, questions[0].factor)

    def test_coverage_per_incident_options_250K(self):
        questions = [Question("COVERAGE_PER_INCIDENT_OPTIONS", "3", 1)]
        quote = InsuranceQuote(questions)
        quote.render_quote()
        self.assertEqual(0.75, questions[0].factor)
