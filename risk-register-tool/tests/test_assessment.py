import unittest
from src.risk.models import Risk
from src.risk.assessment import calculate_risk_score, assess_risk

class TestRiskAssessment(unittest.TestCase):
    def setUp(self):
        self.low = Risk(id=1, title="Low", description="", category="", likelihood=1, impact=2)
        self.medium = Risk(id=2, title="Medium", description="", category="", likelihood=3, impact=3)
        self.high = Risk(id=3, title="High", description="", category="", likelihood=5, impact=5)

    def test_calculate_risk_score(self):
        for risk in [self.low, self.medium, self.high]:
            score = calculate_risk_score(risk)
            print(f"Assessment: {risk.title} risk score is {score}")
            self.assertIsInstance(score, int)

    def test_assess_risk(self):
        for risk in [self.low, self.medium, self.high]:
            assessment = assess_risk(risk)
            print(f"Assessment: {risk.title} risk is {assessment}")
            self.assertIn(assessment, ["Low", "Medium", "High"])

if __name__ == '__main__':
    unittest.main()