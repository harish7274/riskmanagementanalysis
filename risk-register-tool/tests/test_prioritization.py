import unittest
from src.risk.prioritization import prioritize_risks, generate_priority_report
from src.risk.models import Risk

class TestRiskPrioritization(unittest.TestCase):

    def setUp(self):
        self.risks = [
            Risk(id=1, title="Risk A", description="", category="", likelihood=5, impact=10),
            Risk(id=2, title="Risk B", description="", category="", likelihood=3, impact=8),
            Risk(id=3, title="Risk C", description="", category="", likelihood=4, impact=6),
        ]

    def test_prioritize_risks(self):
        prioritized = prioritize_risks(self.risks)
        report = generate_priority_report(prioritized)
        print(f"Prioritization Report:\n{report}")
        self.assertEqual(prioritized[0].title, "Risk A")
        self.assertCountEqual([prioritized[1].title, prioritized[2].title], ["Risk B", "Risk C"])

    def test_empty_risk_list(self):
        prioritized = prioritize_risks([])
        self.assertEqual(prioritized, [])

if __name__ == '__main__':
    unittest.main()